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
    return faces

# we flood the grid with 2s from the outside, this leaves the air pockets intact
mat[0, 0, 0] = 2
while True:
    flag = 0
    for x in range(mat.shape[0]):
        for y in range(mat.shape[1]):
            for z in range(mat.shape[2]):
                # if any neighbor is 2 and block is 0
                if x-1 >= 0 and mat[x, y, z] == 0 and mat[x-1, y, z] == 2:
                    mat[x, y, z] = 2
                    flag = 1
                    continue
                if y-1 >= 0 and mat[x, y, z] == 0 and mat[x, y-1, z] == 2:
                    mat[x, y, z] = 2
                    flag = 1
                    continue
                if z-1 >= 0 and mat[x, y, z] == 0 and mat[x, y, z-1] == 2:
                    mat[x, y, z] = 2
                    flag = 1
                    continue
                if x+1 < mat.shape[0] and mat[x, y, z] == 0 and mat[x+1, y, z] == 2:
                    mat[x, y, z] = 2
                    flag = 1
                    continue
                if y+1 < mat.shape[1] and mat[x, y, z] == 0 and mat[x, y+1, z] == 2:
                    mat[x, y, z] = 2
                    flag = 1
                    continue
                if z+1 < mat.shape[2] and mat[x, y, z] == 0 and mat[x, y, z+1] == 2:
                    mat[x, y, z] = 2
                    flag = 1
                    continue
    if flag == 0:
        break
# we fill in the air pockets with 1s
x_c = 0
for x in range(mat.shape[0]):
    for y in range(mat.shape[1]):
        for z in range(mat.shape[2]):
            if mat[x, y, z] == 0:
                mat[x, y, z] = 1
# and we change all the 2s to 0 so the function from part 1 works
for x in range(mat.shape[0]):
    for y in range(mat.shape[1]):
        for z in range(mat.shape[2]):
            if mat[x, y, z] == 2:
                mat[x, y, z] = 0
result = 0
for i in range(max):
    result += process_row(mat[i], i)
print(result)
