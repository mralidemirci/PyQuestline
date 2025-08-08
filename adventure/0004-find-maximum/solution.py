a = int(input("first number : "))
b = int(input("second number : "))
c = int(input("third number : "))
max = a

if a >= b :
	max = a

else :
	max = b
	
if max >= c:
	print("the max number is : ", max)
		
else :
	print("the max number is : ", c)