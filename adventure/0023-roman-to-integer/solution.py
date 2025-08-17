userInput = input()
numericDict = {'I' : 1 , 'V' : 5 , 'X' : 10, 'L' : 50 , 'C' : 100 , 'D' : 500 , 'M' : 1000}
subtractive_nums = ['I' , 'X' , 'C']
listUserInput = list(userInput)
numericResult = 0

i = 0
while i < len(listUserInput):
	if listUserInput[i] in subtractive_nums:
		if i + 1 < len(listUserInput):
			if numericDict[listUserInput[i+1]] > numericDict[listUserInput[i]]:
				numericResult = numericResult + ( numericDict[listUserInput[i+1]] - numericDict[listUserInput[i]] )
				i += 2
				continue
			if numericDict[listUserInput[i+1]] <= numericDict[listUserInput[i]]:
				numericResult = numericResult + numericDict[listUserInput[i]]
				i += 1
				continue
		else:
			numericResult = numericResult + numericDict[listUserInput[i]]
			i += 1
	else:
		numericResult = numericResult + numericDict[listUserInput[i]]
		i += 1
		continue

print(numericResult)    