def longestIncreasingSubsequence(array):
    length = len(array)
    if not length:
        return
    elif length == 1:
        return array[0]

    SeqLen =[1 for j in range(length)]
    Seq = [-1 for j in range(length)]

    for i in range(1,length):
        for j in range (0,i):
            if array[i] > array[j]:
                temp = SeqLen[j] + 1
                if temp >= SeqLen[i]:
                    SeqLen[i] = temp
                    Seq[i]=j

    SubArr=[]

    for i in reversed(Seq):
        if i == -1:
            break
        else:
            SubArr.append(array[i])


    return SubArr


print(longestIncreasingSubsequence([5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]))
