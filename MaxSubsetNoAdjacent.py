
def maxSubsetSumNoAdjacent(array):
    length = len(array)
    if not length:
        return
    elif length==1:
        return array[0]

    maxSum= array[:]
    maxSum[0] = array[0]
    maxSum[1] = max(array[0],array[1])
    for i in range(2,length):
        maxSum[i] = max(maxSum[i-2]+array[i],maxSum[i-1])

    return maxSum[-1]



print(maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135]))