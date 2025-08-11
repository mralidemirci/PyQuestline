theWord = input()
checkedChars = {}

for ch in theWord:
	checkedChars[ch] = checkedChars.get(ch,0) + 1
	
for ch,count in checkedChars.items():
	if count == 1:
		print(ch)
		break
		
else:
	print("None")