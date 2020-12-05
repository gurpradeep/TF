'''
def twoNumberSum(array, targetSum):
    retArr=[]
    d = {}
    for item in array:
        d[item]=item

    for k,v in d.items():
        elem = targetSum-k
        if elem in d.keys():
            retArr = [k,elem]
            return retArr
    return[]
'''

'''
def twoNumberSum(array, targetSum):
    retArr=[]
    d = {}
    for item in array:
        d[item]=item

    for k,v in d.items():
        elem = targetSum-k
        if elem in d.keys():
            retArr = [k,elem]
            return retArr
    return[]
'''
'''
def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum-num
        if potentialMatch in nums:
            return[potentialMatch,num]
        else:
            nums[num]=True
    return[]
'''


def twoNumberSum(array, targetSum):
    retNum = []
    array.sort()
    nLen = len(array)
    found =0
    left = 0
    right = nLen - 1
    while (found==0):
        if ((array[left] + array[right]) < targetSum):
            left = left + 1
        elif((array[left] + array[right]) > targetSum):
            right = right - 1
        else:
            if((array[left] + array[right])== targetSum):
                found = 1
                retNum = [array[left], array[right]]
        if(left>right):
            found =2
    return retNum

print (twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))