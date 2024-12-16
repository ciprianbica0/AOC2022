import numpy as np


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
tail = []
matrix[r, c] = 1
KNOTS = 9
for i in range(0, KNOTS):
    tail.append([r, c])


def updatetail(tailnum):
    currenttail = tail[tailnum]
    # print("Tail",tailnum," at ",currenttail[0],currenttail[1],'\n')
    if tailnum == KNOTS-1:
        matrix[currenttail[0]][currenttail[1]] = 1


def updateknot(tailnum):
    currenttail = tail[tailnum]
    if tailnum == 0:
        lasttail = head
    else:
        lasttail = tail[tailnum-1]

    if currenttail[0] == lasttail[0] and currenttail[1] == lasttail[1]:
        updatetail(tailnum)
        return

    if currenttail[0] == lasttail[0]:  # head and tail are on the same row
        if lasttail[1] == currenttail[1]+2:
            currenttail[1] += 1
        if lasttail[1] == currenttail[1]-2:
            currenttail[1] -= 1
        updatetail(tailnum)
        return

    if currenttail[1] == lasttail[1]:  # head and tail are on the same column
        if lasttail[0] == currenttail[0]+2:
            currenttail[0] += 1
        if lasttail[0] == currenttail[0]-2:
            currenttail[0] -= 1
        updatetail(tailnum)
        return

    if comp(lasttail[1], currenttail[1]) == -1:
        currenttail[1] -= 1
        if currenttail[0] == lasttail[0]-1:
            currenttail[0] += 1
        if currenttail[0] == lasttail[0]-2:
            currenttail[0] += 1
        if currenttail[0] == lasttail[0]+1:
            currenttail[0] -= 1
        if currenttail[0] == lasttail[0]+2:
            currenttail[0] -= 1
        updatetail(tailnum)
        return

    if comp(lasttail[1], currenttail[1]) == 1:
        currenttail[1] += 1
        if currenttail[0] == lasttail[0]-1:
            currenttail[0] += 1
        if currenttail[0] == lasttail[0]-2:
            currenttail[0] += 1
        if currenttail[0] == lasttail[0]+1:
            currenttail[0] -= 1
        if currenttail[0] == lasttail[0]+2:
            currenttail[0] -= 1
        updatetail(tailnum)
        return

    if comp(lasttail[0], currenttail[0]) == 1:
        currenttail[0] += 1
        if currenttail[1] == lasttail[1]-1:
            currenttail[1] += 1
        if currenttail[1] == lasttail[1]-2:
            currenttail[1] += 1
        if currenttail[1] == lasttail[1]+2:
            currenttail[1] -= 1
        if currenttail[1] == lasttail[1]+1:
            currenttail[1] -= 1
        updatetail(tailnum)
        return

    if comp(lasttail[0], currenttail[0]) == -1:
        currenttail[0] -= 1
        if currenttail[1] == lasttail[1]-1:
            currenttail[1] += 1
        if currenttail[1] == lasttail[1]-2:
            currenttail[1] += 1
        if currenttail[1] == lasttail[1]+2:
            currenttail[1] -= 1
        if currenttail[1] == lasttail[1]+1:
            currenttail[1] -= 1
        updatetail(tailnum)
        return
    # print("no need to move tail ",tailnum)


for line in f:
    line = line.split()
    direction = line[0]
    steps = int(line[1])

    for i in range(steps):
        if direction == "U":
            head[0] -= 1

        if direction == "D":
            head[0] += 1

        if direction == "R":
            head[1] += 1

        if direction == "L":
            head[1] -= 1
        print("head    at ", head[0], head[1])
        for j in range(0, KNOTS):
            updateknot(j)


count = 0
for i in range(1000):
    for j in range(1000):
        if matrix[i][j] == 1:
            count += 1
print(count)
