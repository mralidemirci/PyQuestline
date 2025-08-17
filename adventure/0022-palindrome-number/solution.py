userInput = input()
theList = list(userInput)
tempList = theList.copy()
counter = -1
reverseUserInput = ''

for i in range(len(theList)):
	tempList[counter] = theList[i]
	counter -= 1
	
for i in tempList:
	reverseUserInput = reverseUserInput + i
	
if userInput == reverseUserInput:
	print('YES')
else:
	print('NO')