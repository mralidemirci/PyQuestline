counter = int(input())
nums = input().split()
target = int(input())

for i in range(len(nums)):
	nums[i] = int(nums[i])
	
found = False
for i in range(len(nums)):
	for j in range(i + 1 , len(nums)):
		if nums[i] + nums[j] == target:
			print(i , j)
			found = True
			break
	if found:
		break
else : 
	print("NA")

