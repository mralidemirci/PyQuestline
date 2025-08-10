vowels = ['a','A','e','E','ı','I','i','İ','o','O','ö','Ö','u','U','ü','Ü']
vowelsInString = []

theString = input()

for i in range(len(theString)):
	for j in range(len(vowels)):
		if theString[i] == vowels[j]:
			vowelsInString.append(theString[i])

for i in range(len(vowelsInString)):
	theString = theString.replace(vowelsInString[i], "")
			
print(theString)
			