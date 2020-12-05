'''
def merge_lists(lst1, lst2):
    lstcur1=0
    lstcur2=0
    llst1= len(lst1)
    llst2 = len(lst2)
    totallen = llst1 + llst2
    merged_list=[]
    mergedlen=0
    coveredlst1=0
    coveredlst2 = 0
    while (mergedlen < totallen):
        if lstcur1< llst1 and lstcur2< llst2 and lst1[lstcur1] <= lst2[lstcur2]:
            merged_list.append(lst1[lstcur1])
            lstcur1=lstcur1+1

        if lstcur1< llst1 and lstcur2< llst2 and lst1[lstcur1] >= lst2[lstcur2]:
            merged_list.append(lst2[lstcur2])
            lstcur2=lstcur2+1

        if lstcur1 > llst1-1:
            coveredlst1 = 1;
            if(coveredlst2 == 0):
                merged_list.append(lst2[lstcur2])
                lstcur2 = lstcur2 + 1

        if lstcur2> llst2-1:
            coveredlst2 = 1;
            if(coveredlst1 == 0):
                merged_list.append(lst1[lstcur1])
                lstcur1 = lstcur1 + 1


        mergedlen=mergedlen+1

    return merged_list


print(merge_lists([1,3,4,5],[2,6,7,8]))

print(merge_lists([4,4,4,4],[4,4,4,4]))

print(merge_lists([1,4,45,63],[]))

print(merge_lists([],[1,2,3,4,5]))
'''
'''
def find_product2(lst):
    result = []
    left = 1  # To store product of all previous values from currentIndex
    for i in range(len(lst)):
        currentproduct = 1  # To store current product for index i
        # compute product of values to the right of i index of list
        for ele in lst[i+1:]:
            currentproduct = currentproduct * ele
        # currentproduct * product of all values to the left of i index
        result.append(currentproduct * left)
        # Updating `left`
        left = left * lst[i]

    return result
def find_product(lst):
    # get product start from left
    left = 1
    product = []
    for ele in lst:
        product.append(left)
        left = left * ele
    # get product starting from right
    right = 1
    for i in range(len(lst)-1, -1, -1):
        product[i] = product[i] * right
        right = right * lst[i]

    return product


print(find_product([0, 1, 2, 3]))
print(find_product([1, 2, 3, 4]))
'''
def max_min(lst):
    max_min_lst = []
    nLen = len(lst)
    reverseIndex = nLen - 1
    for i in range(nLen):
        reverseIndex = nLen-1-i
        if (reverseIndex >i):
            max_min_lst.append(lst[reverseIndex])
            max_min_lst.append(lst[i])
        if (reverseIndex == i):
            max_min_lst.append(lst[i])

    return max_min_lst

print(max_min([1,2,3,4,5]))