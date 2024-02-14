import numpy as np
f = open("day14_input.txt", "r")

ROWS = 200
COLS = 700
SAND = [0, 500]
FLOOR = -1
matrix = np.zeros((ROWS, COLS))


def fill_line(A, B):
    matrix[A[0]][A[1]] = 1
    matrix[B[0]][B[1]] = 1
    if A[0] == B[0]:
        k = (A[1]-B[1])
        for i in range(abs(k)):
            if k > 0:
                matrix[A[0]][A[1]-i] = 1
            if k < 0:
                matrix[A[0]][A[1]+i] = 1
    elif A[1] == B[1]:
        k = (A[0]-B[0])
        for i in range(abs(k)):
            if k > 0:
                matrix[A[0]-i][A[1]] = 1
            if k < 0:
                matrix[A[0]+i][A[1]] = 1


for line in f:
    line = line.split(" -> ")
    X = []
    Y = []
    for parts in line:
        parts = parts.split(",")
        X.append(int(parts[1]))
        Y.append(int(parts[0]))
        FLOOR = max(FLOOR, int(parts[1]))
    for i in range(len(X)-1):
        A = [X[i], Y[i]]
        B = [X[i+1], Y[i+1]]
        fill_line(A, B)

FLOOR += 2
for i in range(COLS):
    matrix[FLOOR][i] = 1

# block = ""
# for i in range(0, 12):
#     for j in range(490, 510):
#         block += '.' if matrix[i][j] == 0 else '#'
#         block += " "
#     block += "\n"
# print(block)


def generate_sand():
    outcome = check_if_falling(SAND[0], SAND[1])
    while outcome != 100 and outcome != 0:
        outcome = check_if_falling(SAND[0], SAND[1])
        if outcome != 100 and outcome != 0:
            SAND[0] += 1
            if outcome == 1 or outcome == -1:
                SAND[1] += outcome
            if outcome == 404:
                return 0
    if outcome == 0:
        if SAND[0] == 0 and SAND[1] == 500:
            matrix[SAND[0]][SAND[1]] = 2
            return 0
        # print(SAND[0],SAND[1])
        matrix[SAND[0]][SAND[1]] = 2
        SAND[0] = 0
        SAND[1] = 500
        return 1
    if outcome == 100:
        return 0


def is_solid(x, y):
    if matrix[x][y] == 1 or matrix[x][y] == 2:
        return 1
    else:
        return 0


def check_if_falling(x, y):
    if x > ROWS:
        return 404
    if x+1 in range(ROWS):
        if y-1 in range(COLS) and y in range(COLS) and y+1 in range(COLS):
            if is_solid(x+1, y):
                if is_solid(x+1, y-1):
                    if is_solid(x+1, y+1):
                        return 0  # sand can rest
                    else:
                        return 1  # block to the side is not solid
                else:
                    return -1  # block to the side is not solid
            else:
                return 2  # block below is not solid
    else:
        return 100  # fell off the map

result = 1
while result==1:
    result = generate_sand()

block = ""
for i in range(0, 12):
    for j in range(490, 510):
        block += '.' if matrix[i][j] == 0 else (
            '0' if matrix[i][j] == 2 else '#')
        block += " "
    block += "\n"
print(block)

c = 0
for i in range(ROWS):
    for j in range(COLS):
        if matrix[i][j] == 2:
            c += 1
print(c)
