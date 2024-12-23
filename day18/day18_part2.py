import numpy as np

file = open('day18\\day18_input.txt', 'r')
lines = file.read

max = 0
for lines in file:
    lines = lines.split(',')
    for i in lines:
        i = int(i)
        if i > max:
            max = i
print("max is: ", max)

max += 1
mat = np.zeros((max, max, max))

with open("day18\\day18_input.txt") as file:
    lines = [line.rstrip() for line in file]
    for line in lines:
        l = line.split(',')
        n1 = int(l[0])
        n2 = int(l[1])
        n3 = int(l[2])
        mat[n1, n2, n3] = 1

print(mat)


def process_row(layer_matrix, layer_no):
    faces = 0
    # count upwards faces
    a = layer_matrix.shape[0]
    b = layer_matrix.shape[1]

    if layer_no > 0:
        for x in range(a):
            for y in range(b):
                if layer_matrix[x, y] == 1 and mat[layer_no-1, x, y] == 0:
                    faces += 1
    else:
        for x in range(a):
            for y in range(b):
                if layer_matrix[x, y] == 1:
                    faces += 1
    # print("Up",faces)
    # _____________________________________________________________________________
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # _____________________________________________________________________________
    # count downwards faces
    if layer_no < max-1:
        for x in range(a):
            for y in range(b):
                if layer_matrix[x, y] == 1 and mat[layer_no + 1, x, y] == 0:
                    faces += 1
    else:
        for x in range(a):
            for y in range(b):
                if layer_matrix[x, y] == 1:
                    faces += 1
    # print("Down+Up",faces)
    # _____________________________________________________________________________
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # _____________________________________________________________________________
    # count side faces
    for x in range(a):
        for y in range(b):
            if layer_matrix[x, y] == 1:
                if x+1 == max or layer_matrix[x+1, y] == 0:
                    faces += 1
                if x == 0 or layer_matrix[x-1, y] == 0:
                    faces += 1
                if y+1 == max or layer_matrix[x, y+1] == 0:
                    faces += 1
                if y == 0 or layer_matrix[x, y-1] == 0:
                    faces += 1
            # SEE IF WE HAVE TRAPPED AIR
            if layer_matrix[x, y] == 0 and layer_matrix[x+1, y] and layer_matrix[x-1, y]:
                if layer_matrix[x, y+1] and layer_matrix[x, y-1]:
                    if mat[layer_no-1, x, y] and mat[layer_no+1, x, y]:

    return faces


result = 0
for i in range(max):
    result += process_row(mat[i], i)
print(result)
