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
        numbas = re.findall(r'(\d+)', line)
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


def find_first_one(row_number):
    row = m[row_number]
    for i in range(len(row)):
        if row[i] == 1:
            return i
    return -1


numbas = list(map(int, numbas))

# face_1 = [[0, 50], [0, 99], [49, 50], [49, 99]]
# face_2 = [[0, 100], [0, 149], [49, 100], [49, 149]]
# face_3 = [[50, 50], [50, 99], [99, 50], [99, 99]]
# face_4 = [[100, 0], [100, 49], [149, 0], [149, 49]]
# face_5 = [[100, 50], [100, 99], [149, 50], [149, 99]]
# face_6 = [[150, 0], [150, 49], [199, 0], [199, 49]]


def determine_face(x, y):
    if x >= 0 and x <= 49:
        if y >= 50 and y <= 99:
            return 1
        if y >= 100 and y <= 149:
            return 2
    if x >= 50 and x <= 99 and y >= 50 and y <= 99:
        return 3
    if x >= 100 and x <= 149:
        if y >= 0 and y <= 49:
            return 4
        if y >= 50 and y <= 99:
            return 5
    if x >= 150 and x <= 199:
        return 6


def determine_dir(curr_dir, target_dir):
    if curr_dir == "R":
        if target_dir == "R":
            return "D"
        else:
            return "U"
    if curr_dir == "D":
        if target_dir == "L":
            return "R"
        else:
            return "L"
    if curr_dir == "U":
        if target_dir == "R":
            return "R"
        else:
            return "L"
    if curr_dir == "L":
        if target_dir == "L":
            return "D"
        else:
            return "U"
    return "F"

# 1D 3D
# 1R 2R
# 1U 6R
# 1L 4R

# 2U 6U
# 2D 3L
# 2L 1L
# 2R 5L

# 3D 5D
# 3U 1U
# 3L 4D
# 3R 2U

# 4D 6D
# 4U 3R
# 4R 5R
# 4L 1R

# 5U 3U
# 5D 6L
# 5L 4L
# 5R 2L

# 6D 2D
# 6U 4U
# 6L 1D
# 6R 5U


def edge_walk(coords, dir):
    x = coords[0]
    y = coords[1]
    nface = 0
    ndir = 0
    nx = 0
    ny = 0
    face = determine_face(x, y)
    if face == 1 and dir == 'U' and x == 0:
        nface, ndir, nx, ny = 6, 'R', y + 100, 0
    elif face == 1 and dir == 'L' and y == 50:
        nface, ndir, nx, ny = 4, 'R', 149 - x, 0

    elif face == 2 and dir == 'U' and x == 0:
        nface, ndir, nx, ny = 6, 'U', 199, y - 100
    elif face == 2 and dir == 'R' and y == 149:
        nface, ndir, nx, ny = 5, 'L', 149 - x, 99
    elif face == 2 and dir == 'D' and x == 49:
        nface, ndir, nx, ny = 3, 'L', y - 50, 99

    elif face == 3 and dir == 'L' and y == 50:
        nface, ndir, nx, ny = 4, 'D', 100, x - 50
    elif face == 3 and dir == 'R' and y == 99:
        nface, ndir, nx, ny = 2, 'U', 49, x + 50

    elif face == 4 and dir == 'U' and x == 100:
        nface, ndir, nx, ny = 3, 'R', y + 50, 50
    elif face == 4 and dir == 'L' and y == 0:
        nface, ndir, nx, ny = 1, 'R', 149 - x, 50

    elif face == 5 and dir == 'R' and y == 99:
        nface, ndir, nx, ny = 2, 'L', 149 - x, 149
    elif face == 5 and dir == 'D' and x == 149:
        nface, ndir, nx, ny = 6, 'L', y + 100, 49

    elif face == 6 and dir == 'L' and y == 0:
        nface, ndir, nx, ny = 1, 'D', 0, x - 100
    elif face == 6 and dir == 'R' and y == 49:
        nface, ndir, nx, ny = 5, 'U', 149, x - 100
    elif face == 6 and dir == 'D' and x == 199:
        nface, ndir, nx, ny = 2, 'D', 0, y + 100

    else:
        return None

    if m[nx][ny] == 2:
        return "wall"
    return nface, ndir, nx, ny


def walk(pos, dir, steps):
    x = pos[0]
    y = pos[1]

    for _ in range(steps):
        nx, ny = x, y
        ndir = dir

        if dir == "R":
            ny += 1
        elif dir == "L":
            ny -= 1
        elif dir == "D":
            nx += 1
        else:
            nx -= 1

        if nx < 0 or nx >= rows or ny < 0 or ny >= cols or m[nx][ny] == 0:
            wrapped = edge_walk((x, y), dir)
            if wrapped is None or wrapped == "wall":
                return (x, y), dir
            _, ndir, nx, ny = wrapped

        if m[nx][ny] == 2:
            return (x, y), dir

        x, y, dir = nx, ny, ndir

    return (x, y), dir


pos = [0, find_first_one(0), "R"]
current_pos = (pos[0], pos[1])
current_dir = pos[2]
last_dir = "F"

for i in range(len(numbas)):
    if i < len(dirs):
        current_pos, current_dir = walk(
            current_pos, current_dir, numbas[i])
        current_dir = determine_dir(current_dir, dirs[i])
        last_dir = current_dir
    else:
        current_pos, current_dir = walk(
            current_pos, current_dir, numbas[i])
        last_dir = current_dir

current_pos = tuple(x + 1 for x in current_pos)

facing = {"R": 0, "D": 1, "L": 2, "U": 3}[last_dir]

final_password = 1000*current_pos[0] + 4 * current_pos[1] + facing
print("Final password:", final_password)
