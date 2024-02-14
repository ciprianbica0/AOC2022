from copy import deepcopy
import numpy as np

f = open("day12_input.txt", "r")
matrix = []
ROWS = 0
COLS = 0
S = [0, 0]
E = [0, 0]
for line in f:
    row = []
    for c in line:
        if c != '\n':
            row.append(c)
    matrix.append(row)
matrix = np.array(matrix, dtype=object)
ROWS, COLS = matrix.shape
previous = deepcopy(matrix)
for i in range(ROWS):
    for j in range(COLS):
        if matrix[i][j] == 'S':
            S[0] = i
            S[1] = j
        if matrix[i][j] == 'E':
            E[0] = i
            E[1] = j
        previous[i][j] = [0, 0]
steps = [[S[0], S[1]]]

matrix[S[0]][S[1]] = 'a'


def BFS(matrix, root):
    queue = []
    explored = [root]
    queue.append(root)
    while len(queue) != 0:
        v = queue.pop(0)
        if matrix[v[0]][v[1]] == 'E':
            return v
        neighbors = []
        x, y = v[0], v[1]
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:  # GENIUS!!!!!!
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < ROWS and 0 <= new_y < COLS and ((abs(ord(matrix[x][y]) - ord(matrix[new_x][new_y])) <= 1 or (ord(matrix[x][y]) - ord(matrix[new_x][new_y])) > 0 and matrix[new_x][new_y] != 'E') or (matrix[new_x][new_y] == 'E' and matrix[x][y] == 'z')):
                neighbors.append([new_x, new_y])
        for w in neighbors:
            if w not in explored:
                explored.append(w)
                previous[w[0]][w[1]] = [v[0], v[1]]
                queue.append(w)


a = []
for i in range(ROWS):
    for j in range(COLS):
        if matrix[i, j] == 'a' and (BFS(matrix, [i, j]))!=None:
            print(i,j)
            b = 0
            current = deepcopy(E)
            while not (current[0] == i and current[1] == j):
                b += 1
                # print(b)
                current = previous[current[0]][current[1]]
                # print(matrix[current[0], current[1]])
            a.append(b)
print(min(a))
