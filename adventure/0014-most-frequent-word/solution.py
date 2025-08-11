theList = input().split()
uniqueWords = []
theDict = {}

for word in theList:
	found = False
	for a in uniqueWords:
		if word == a:
			found = True
			
	if found != True:
		uniqueWords.append(word)
		
for word in uniqueWords:
	counter = 0
	for a in theList:
		if word == a:
			counter += 1
			
	theDict[word] = counter
	
for key,value in theDict.items():
	print(f"{key} : {value}")