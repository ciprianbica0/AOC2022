import pip
import numpy as np

f = open("day8\\day8_input.txt", "r")
matrix = []
visible = 0
for line in f:
    row = []
    for c in line:
        if c != '\n':
            row.append(int(c))
    matrix.append(row)
matrix = np.array(matrix)

for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        if i == 0 or j == 0 or i == matrix.shape[0]-1 or j == matrix.shape[1]-1:
            visible += 1

        else:
            top = True
            bottom = True
            left = True
            right = True
            # check from top
            for vert in range(0, i):
                if matrix[vert][j] >= matrix[i][j]:
                    top = False
            for vert in range(i+1, matrix.shape[0]):
                if matrix[vert][j] >= matrix[i][j]:
                    bottom = False
            for lat in range(0, j):
                if matrix[i][lat] >= matrix[i][j]:
                    left = False
            for lat in range(j+1, matrix.shape[1]):
                if matrix[i][lat] >= matrix[i][j]:
                    right = False
            if top or bottom or left or right:
                visible += 1

print(visible)
