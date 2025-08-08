from collections import namedtuple

counter = int(input())
columns = input().split()
theTable = namedtuple("Table", columns)
sum = 0
stCount = 0

while counter > 0 :
	stData = input().split()
	st = theTable(*stData)
	counter = counter - 1
	stCount = stCount + 1
	sum = sum + int(st.MARKS)
	
print(f"{sum / stCount:.2f}") 