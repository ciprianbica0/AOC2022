import math

f = open("AoC2022/Day4/day4.txt", "r")
counter = 0
data = f.readlines()
for i in range(0,len(data)):
    l = data[i].split('-')
    start1 = int(l[0])
    l1 = l[1].split(',')
    end1 = int(l1[0])
    start2 = int(l1[1])
    l2 = l[2].split('/')
    end2 = int(l2[0])
    elf1 = range(start1,end1+1)
    elf2 = range(start2,end2+1)
    for j in elf1:
        if j in elf2:
            counter+=1
            break
print(counter)