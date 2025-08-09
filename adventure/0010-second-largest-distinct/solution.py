counter = int(input())
list = []
repeatedNumbers = []

while counter > 0:
	theNumber = int(input())
	list.append(theNumber)
	counter -= 1
	
for i in range(len(list)):
	miniCounter = 1
	if i != len(list) -1:
		for j in range(i+1, len(list)):
			if list[i] == list[j]:
				while miniCounter != 0:
					repeatedNumbers.append(list[i])
					miniCounter -= 1
	else:
		break

for i in repeatedNumbers:
	list.remove(i)

for i in range(len(list)):
	theMax = list[i]
	for j in range(len(list)):
		if list[j] > theMax:
			theMax = list[j]
			list[j] = list[i]
			list[i] = theMax
			

if len(list) < 2:
	print("NA")
else:
	theSecondlargest = list[len(list) - 2]
	print(theSecondlargest)