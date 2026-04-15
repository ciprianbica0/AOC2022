import math

f = open("AoC2022/Day3/day3.txt", "r")
totalpriority = 0
data = f.readlines()
for i in range(0,len(data)-2,3):
    elf1 = data[i]
    elf2 = data[i+1]
    elf3 = data[i+2]
    for c in elf1:
        if c in elf2:
            if c in elf3:
                if c >= 'A' and c<= 'Z':
                    totalpriority += ord(c)-38
                if c >= 'a' and c<= 'z':
                    totalpriority += ord(c)-96
                break

print(totalpriority)