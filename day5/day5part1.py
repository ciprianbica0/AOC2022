import math

f = open("AoC2022/Day5/day5.txt", "r")
stacks = []
data = f.readlines()
for i in range(0, math.ceil((len(data[0])+1)/4)-1):
    stacks.append([])

for i in range(0, len(data)):
    if (data[i].find('[') != -1):
        stackpointer = 1
        for j in range(1, len(data[i]), 4):
            if data[i][j] == ' ':
                stackpointer += 1
            else:
                stacks[stackpointer-1].append(data[i][j])
                stackpointer += 1

    if (data[i].startswith(" 1")):
        for c in stacks:
            c.reverse()

    elif data[i].startswith('move'):
        l = data[i].split(' ')
        source = int(l[3])-1
        destination = int(l[5])-1
        quantity = int(l[1])
        for c in range(0, quantity):
            stacks[destination].append(stacks[source].pop())
result = ""
for i in stacks:
    result += (i[len(i)-1])
print(result)
