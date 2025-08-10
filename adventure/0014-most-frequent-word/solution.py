theSentences = input().split()
checkedWords = []
theWord = ""
maxCount = 1

for i in range(len(theSentences)):
	wordCount = 1
	for j in range(i+1, len(theSentences)):
		if theSentences[i] == theSentences[j]:
			wordCount += 1
			if wordCount > maxCount:
				maxCount = wordCount
				theWord = theSentences[i]

if maxCount == 1:
    print("No repetitions found")
else:
    print(theWord)