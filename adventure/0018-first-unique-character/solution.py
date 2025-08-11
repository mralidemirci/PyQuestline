theWord = input()
checkedChars = {}

for i in range(len(theWord)):
	counter = 1
	if theWord[i] not in checkedChars:
		for j in range(i+1 , len(theWord)):
				if theWord[i] == theWord[j]:
					counter += 1
		checkedChars[theWord[i]] = counter

counter = 0		
for key,value in checkedChars.items():
	if value != 1:
		counter += 1

if counter == len(checkedChars):
	print("None")

elif counter != len(checkedChars):
	for key,value in checkedChars.items():
		if value == 1:
			print(key)
			break