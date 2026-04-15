f = open("AoC2022/Day1/day1.txt", "r")

elf = 1
maxelf = -1
currentsum = 0
max1 = 0
totalcalorieslist = []
for i in f:
    if i == '\n':
        if currentsum > max1:
            max1 = currentsum
            maxelf = elf
        totalcalorieslist.append(currentsum)
        currentsum = 0
        elf = elf+1
    else:
        currentsum = currentsum + int(i)
totalcalorieslist.sort()
result = totalcalorieslist.pop()+totalcalorieslist.pop()+totalcalorieslist.pop()
print(result)
