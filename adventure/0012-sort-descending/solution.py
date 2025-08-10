counter = int(input())
numbers = []

while counter > 0:
	numbers.append(int(input()))
	counter -= 1
	
for i in range(len(numbers)):
	for j in range(i+1, len(numbers)):
		if numbers[i] <= numbers[j]:
			tempMax = numbers[i]
			numbers[i] = numbers[j]
			numbers[j] = tempMax
			
print(*numbers)
			