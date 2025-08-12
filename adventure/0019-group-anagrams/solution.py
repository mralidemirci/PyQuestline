count = int(input())
wordList = []
xList = []
myDict = {}

for i in range(count):
    wordList.append(input())

for word in wordList:
    xDict = {}
    for i in word:
        xDict[i] = xDict.get(i, 0) + 1
    myDict[word] = xDict

tempWordList = wordList.copy()

for i in range(len(wordList)):
    printList = []
    if wordList[i] in tempWordList:
        printList.append(wordList[i])
        for j in range(i + 1, len(wordList)):
            if myDict[wordList[i]] == myDict[wordList[j]]:
                printList.append(wordList[j])
    if printList:
        print(*printList)
    for item in printList:
        tempWordList.remove(item)