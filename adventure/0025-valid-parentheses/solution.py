xInput = input()

input_list = list(xInput)
para_list = [( '(' , ')' ), ( '[' , ']' ), ( '{' , '}' )]
counter = 0
openings = ['(', '[', '{']

for a in input_list:
    if a in openings:
        counter += 1

found = False
firstDeleteIndex = ''
secondDeleteIndex = ''

for k in range(counter):
    jobDone = False

    for i in range(len(input_list)):
        for j in range(len(para_list)):
            if i + 1 < len(input_list) and jobDone == False:
                if input_list[i] == para_list[j][0] and input_list[i+1] == para_list[j][1]:
                    firstDeleteIndex = i + 1
                    secondDeleteIndex = i
                    found = True
                    jobDone = True

    if found:
        del input_list[firstDeleteIndex]
        del input_list[secondDeleteIndex]
        found = False
                
if input_list:
    print("NO")
else:
    print("YES")
