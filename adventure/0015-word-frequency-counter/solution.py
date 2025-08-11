theList = ["ali", "demirci", "ali", "veli", "demirci", "ali"]
words = []
theDict = {}

for a in theList:
	weHave = False
	for b in range(len(theList)):
		if a == theList[b]:
			weHave = True
			
	if weHave == False:
		words.append(a)
			
print(words)