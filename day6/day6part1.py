import math

f = open("AoC2022/Day6/day6.txt", "r")
data = f.readline()
result = 4
for i in range(3, len(data)):
    ch1 = data[i-3]
    ch2 = data[i-2]
    ch3 = data[i-1]
    ch4 = data[i]
    if ch1 == ch2 or ch1 == ch3 or ch1 == ch4:
        result += 1
        continue
    elif ch2 == ch1 or ch2 == ch3 or ch2 == ch4:
        result += 1
        continue
    elif ch3 == ch1 or ch2 == ch3 or ch3 == ch4:
        result += 1
        continue
    elif ch4 == ch1 or ch4 == ch3 or ch2 == ch4:
        result += 1
        continue
    print(result)
    break
