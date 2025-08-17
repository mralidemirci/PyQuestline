theWord = input()

result = ""
counter = -1
isNegative = False

if theWord[0] == '-':
	theWord = theWord[1:]
	isNegative = True
	
num=list(theWord)
newNum = num.copy()

for i in range(len(num)):
	newNum[counter] = num[i]
	counter -= 1

for i in newNum:
	result = result + i

result = int(result)

if isNegative:
	result = result * -1
	
if -2**31 <= result <= 2**31 - 1:
	print(result)

else:
	print("0")