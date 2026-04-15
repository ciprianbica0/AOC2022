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
    if start1<=start2 and end1>= end2:
        print(start1,end1,start2,end2)
        counter += 1
    elif start2<=start1 and end2>= end1:
        print(start1,end1,start2,end2)
        counter += 1
print(counter)