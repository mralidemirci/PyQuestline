counter = int(input())
word_list = []
shortest_word = ""
common_prefix = []

for i in range(counter):
	word_list.append(input())
	
shortest_word = word_list[0]
for i in word_list:
	if len(i) < len(shortest_word):
		shortest_word = i
		
for i in range(len(shortest_word)):
	counter = 0
	for j in word_list:
		if shortest_word[i] == j[i]:
			counter += 1
	
	if counter == len(word_list):
		common_prefix.append(shortest_word[i])
		
	else:
		break

print(*common_prefix, sep="")