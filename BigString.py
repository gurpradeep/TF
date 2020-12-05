def compareWords(left, right):#small, word
    exists=False
    index =0
    lLeft = len(left)
    lRight = len(right)
    reverseIndex=0 #suffixCheck
    reveseCheck = False
    reverseLeft = left
    if(lRight>lLeft):
        reveseCheck = True
        for i in range(lRight - lLeft):
            reverseLeft = ' ' + reverseLeft


    if(lLeft <= lRight):
        for l in range(lLeft):
            if (left[l]==right[l]):
                index=index+1
                continue
        if(reveseCheck is True):
            reversed_range = range(lRight-1,0,-1)
            for rev in reversed_range:
                if (reverseLeft[rev]==right[rev]):
                    reverseIndex=reverseIndex+1
                    continue

        if(index==lLeft or reverseIndex==lLeft):
            exists=True
    return exists

def validateParts(words,small ):
    validate =False
    for word in words:
        validate = compareWords(small, word)
        if validate is False:
            continue
        else:
            break
    return validate

def multiStringSearch(bigString, smallStrings):

    boolPresent=[]
    wordsDict={}
    word=''
    bigString=bigString+' '
   # smallStrings = [small.lower() for small in smallStrings]
    first=0
    for char in bigString:
        if char!=' ' :
            #char2 = char.lower()
            word = word+char
        else:
            wordsDict[word]=word
            word=''

    for small in smallStrings:
        if small in wordsDict:
            boolPresent.append(True)
        else:
            boolPresent.append(validateParts(wordsDict.keys(),small))

    return boolPresent

print(multiStringSearch("Mary goes to the shopping center every week.", ["to", "Mary", "centers", "shop", "shopping", "string", "kappa"]))
print(multiStringSearch("this ain't a big string.", ["everything", "inn", "that", "testers", "shall", "failure"]))
print(multiStringSearch("Everything in this test should fail.", ["everything", "inn", "that", "testers", "shall", "failure"]))
print(multiStringSearch("test testing testings tests testers test-takers.", [ "tests","testatk","testiing","trsatii","test-taker","test"]))
print(multiStringSearch("Is this particular test going to pass or is it going to fail? That is the question.", ["that","the","questions","goes","mountain","passes","passed","going","is"]))
print(multiStringSearch("this ain't a big string", ["this", "is", "yo", "a", "bigger"]))
