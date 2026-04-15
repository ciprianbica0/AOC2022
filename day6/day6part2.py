import math

f = open("AoC2022/Day6/day6.txt", "r")
data = f.readline()
result = 14
for i in range(14, len(data)):
    chlist = []
    for j in range(0, 14):
        chlist.append(data[i-j])
    if (len(chlist) == len(set(chlist))):
        print(chlist)
        result += 1
        print(result)
        break
    result += 1
