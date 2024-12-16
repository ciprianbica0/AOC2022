import pip
import numpy as np

f = open("day8\\day8_input.txt", "r")
matrix = []
max_score = 0
for line in f:
    row = []
    for c in line:
        if c != '\n':
            row.append(int(c))
    matrix.append(row)
matrix = np.array(matrix)

for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        score = 0
        if i == 0 or j == 0 or i == matrix.shape[0]-1 or j == matrix.shape[1]-1:
            score = 0

        else:
            top = 0
            bottom = 0
            left = 0
            right = 0
            # check from top
            for vert in range(i-1, -1, -1):
                if matrix[vert][j] >= matrix[i][j]:
                    top += 1
                    break
                else:
                    top += 1
            for vert in range(i+1, matrix.shape[0]):
                if matrix[vert][j] >= matrix[i][j]:
                    bottom += 1
                    break
                else:
                    bottom += 1
            for lat in range(j-1, -1, -1):
                if matrix[i][lat] >= matrix[i][j]:
                    left += 1
                    break
                else:
                    left += 1
            for lat in range(j+1, matrix.shape[1]):
                if matrix[i][lat] >= matrix[i][j]:
                    right += 1
                    break
                else:
                    right += 1
            score = top*bottom*left*right
        max_score = max(score, max_score)

print(max_score)
