import pip
import numpy as np
import time


def comp(a, b):
    if a == b-2:
        return -1
    if a == b+2:
        return 1


f = open("day9\\day9_input.txt", "r")
matrix = np.zeros((1000, 1000), np.int32)
r = 500
c = 500
head = [r, c]
tail = [r, c]
matrix[r, c] = 1
c = 0
oldhead = [r, c]


def updatetail():
    print("Tail at ", tail[0], tail[1], '\n')
    matrix[tail[0]][tail[1]] = 1


for line in f:
    line = line.split()
    direction = line[0]
    steps = int(line[1])

    for i in range(steps):
        oldhead[0] = head[0]
        oldhead[1] = head[1]
        c += 1
        if direction == "U":
            head[0] -= 1

        if direction == "D":
            head[0] += 1

        if direction == "R":
            head[1] += 1

        if direction == "L":
            head[1] -= 1
        print("Head at ", head[0], head[1])
        flag = False

        if tail[0] == head[0]:
            if tail[1] == head[1]:
                updatetail()
                continue

        if tail[0] == head[0]:  # head and tail are on the same row
            if head[1] == tail[1]+2:
                print(1, 2)
                flag = True
                tail[1] += 1
            if head[1] == tail[1]-2:
                flag = True
                print(1, 3)
                tail[1] -= 1
            updatetail()
            continue

        if tail[1] == head[1]:  # head and tail are on the same column
            if head[0] == tail[0]+2:
                flag = True
                print(2, 1)
                tail[0] += 1
            if head[0] == tail[0]-2:
                flag = True
                print(2, 1)
                tail[0] -= 1
            updatetail()
            continue

        if comp(head[0], tail[0]) == -1:  # head is up
            tail[0] = oldhead[0]
            tail[1] = oldhead[1]
            updatetail()
            continue

        if comp(head[0], tail[0]) == 1:  # head is down
            print(4)
            tail[0] = oldhead[0]
            tail[1] = oldhead[1]
            updatetail()
            continue

        if comp(head[1], tail[1]) == 1:  # head is to the right
            tail[0] = oldhead[0]
            tail[1] = oldhead[1]
            updatetail()
            continue

        if comp(head[1], tail[1]) == -1:  # head is to the left
            tail[0] = oldhead[0]
            tail[1] = oldhead[1]
            updatetail()
            continue
        else:
            if not flag:
                print("Tail at ", tail[0], tail[1])
                print("no need to move", '\n')

print(c, " steps")

count = 0
for i in range(1000):
    for j in range(1000):
        if matrix[i][j] == 1:
            count += 1
print(count)
