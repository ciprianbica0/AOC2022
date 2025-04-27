import re
import numpy as np

file = open('day22\\day22_input.txt', 'r')

dirs = []
m = []
rows = 0
cols = 0
map_stop = False
numbas = []

for line in file:
    if line != '\n' and not map_stop:
        rows += 1
        cols = len(line)-1 if len(line)-1 >= cols else cols
    else:
        map_stop = True

    if map_stop:
        m = np.zeros((rows, cols), dtype=int)
        numbas = re.findall("(\d+)", line)  # type: ignore
        for char in line:
            if char == "L":
                dirs.append("L")
            if char == "R":
                dirs.append("R")
m = np.zeros((rows, cols), dtype=int)

count = 0
map_stop = False
file = open('day22\\day22_input.txt', 'r')
for line in file:
    if line != '\n' and not map_stop:
        for c in range(len(line)):
            if line[c] == ".":
                m[count][c] = 1
            if line[c] == "#":
                m[count][c] = 2
        count += 1

    else:
        map_stop = True

# print(numbas)
# print(dirs)
print(m)
print(m.shape)
