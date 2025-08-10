import random

theNumber = random.randint(1,100)
guess = ""
attempt = 0

while guess != theNumber:
	guess = int(input())
	if guess > theNumber:
		print("Lower")
	elif guess < theNumber:
		print("Higher")
	attempt += 1

if guess == theNumber:
	print("Correct! Attempts : ", attempt)
	