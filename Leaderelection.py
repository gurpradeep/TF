import etcd3
import sys
import time

from threading import *

LEADER_KEY = "/myleader"

def main(server_name):
    client = etcd3.client (host="localhost", port=2379)

    while True:
        is_leader, lease = leader_election(client, server_name)

        if(is_leader):
            print("I am the leader")
            on_leadership_gained(lease)
        else:
            print("I am a follower")
            wait_for_next_election(client)

def leader_election(client, server_name):

    print("New leader_election happening.")

    try:
        lease = client.lease(5)
    except:
        print("Unexpected error:", sys.exc_info()[0])

    is_leader = try_insert(client,LEADER_KEY,server_name,lease)
    return is_leader,lease


def try_insert(client,key,value,lease):
    insert_succeeded,_=client.transaction(failure=[],success = [client.transactions.put(key,value,lease)],compare =[client.transactions.version(key) ==0],)
    return insert_succeeded

def on_leadership_gained(lease):

    while True:
        try:
            print("Refreshing lease; still the leader.")
            lease.refresh()
            do_work()

        except Exception:
            lease.revoke()
            return
        except KeyboardInterrupt:
            print("\n Revoking lease;no longer the leader")
            lease.revoke()
            sys.exit(1)

def wait_for_next_election(client):
    election_event = Event()

    def watch_callback(resp):
        for event in resp.events:
            if isintance(event,etcd3.events.DeleteEvent):
                print("Leadership Change Required")
                election_event.set()

    watch_id = client.add_watch_callback(LEADER_KEY,watch_callback)

    try:
        while not election_event.is_set():
            time.sleep(1)

    except KeyBoardInterrupt:
        client.cancel_watch(watch_id)
        sys.exit(1)

    client.cancel_watch(watch_id)





def do_work():
    time.sleep(1)

if __name__=="__main__":
    server_name = sys.argv[1]
    main(server_name)

