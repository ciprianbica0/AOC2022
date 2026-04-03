import copy
import re
import numpy as np

file = open('day22\\day22_input.txt', 'r')

dirs = []
m = np.zeros((0, 0), dtype=int)
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


numbas = list(map(int, numbas))


def walk_right(current_pos, steps):
    last_viable_pos = copy.deepcopy(current_pos)
    row_pos = current_pos[0]
    col_pos = current_pos[1]
    horizon = m[row_pos]
    i = 1
    while i <= steps:
        col_pos %= len(horizon)
        if horizon[(i+col_pos) % len(horizon)] == 2:
            return last_viable_pos
        elif horizon[(i+col_pos) % len(horizon)] == 0:
            col_pos += 1
        elif horizon[(i+col_pos) % len(horizon)] == 1 and i == steps:
            return row_pos, (i+col_pos) % len(horizon)
        elif horizon[(i+col_pos) % len(horizon)] == 1:
            last_viable_pos = copy.deepcopy(
                (row_pos, (i+col_pos) % len(horizon)))
            if i == steps:
                return last_viable_pos
            i += 1


def walk_left(current_pos, steps):
    last_viable_pos = copy.deepcopy(current_pos)
    row_pos = current_pos[0]
    col_pos = current_pos[1]
    horizon = m[row_pos]
    i = 1
    while i <= steps:
        col_pos %= len(horizon)
        if horizon[(col_pos-i) % len(horizon)] == 2:
            return last_viable_pos
        elif horizon[(col_pos-i) % len(horizon)] == 0:
            col_pos -= 1
        elif horizon[(i+col_pos) % len(horizon)] == 1 and i == steps:
            return row_pos, (col_pos-i) % len(horizon)
        elif horizon[(col_pos-i) % len(horizon)] == 1:
            last_viable_pos = copy.deepcopy(
                (row_pos, (col_pos-i) % len(horizon)))
            if i == steps:
                return last_viable_pos
            i += 1


def walk_up(current_pos, steps):
    last_viable_pos = copy.deepcopy(current_pos)
    row_pos = current_pos[0]
    col_pos = current_pos[1]
    horizon = m[:, col_pos]
    i = 1
    while i <= steps:
        col_pos %= len(horizon)
        if horizon[(row_pos-i) % len(horizon)] == 2:
            return last_viable_pos
        elif horizon[(row_pos-i) % len(horizon)] == 0:
            row_pos -= 1
        elif horizon[(i-row_pos) % len(horizon)] == 1 and i == steps:
            return (row_pos-i) % len(horizon), col_pos
        elif horizon[(row_pos-i) % len(horizon)] == 1:
            last_viable_pos = copy.deepcopy((
                (row_pos-i) % len(horizon), col_pos))
            if i == steps:
                return last_viable_pos
            i += 1


def walk_down(current_pos, steps):
    last_viable_pos = copy.deepcopy(current_pos)
    row_pos = current_pos[0]
    col_pos = current_pos[1]
    horizon = m[:, col_pos]
    i = 1
    while i <= steps:
        col_pos %= len(horizon)
        if horizon[(row_pos+i) % len(horizon)] == 2:
            return last_viable_pos
        elif horizon[(row_pos+i) % len(horizon)] == 0:
            row_pos += 1
        elif horizon[(i+row_pos) % len(horizon)] == 1 and i == steps:
            return (row_pos+i) % len(horizon), col_pos
        elif horizon[(row_pos+i) % len(horizon)] == 1:
            last_viable_pos = copy.deepcopy((
                (row_pos+i) % len(horizon), col_pos))
            if i == steps:
                return last_viable_pos
            i += 1


def walk(current_pos, curr_dir, steps, target_dir):
    if curr_dir == "R":
        if target_dir == "R":
            return walk_right(current_pos, steps), "D"
        else:
            return walk_right(current_pos, steps), "U"
    if curr_dir == "D":
        if target_dir == "L":
            return walk_down(current_pos, steps), "R"
        else:
            return walk_down(current_pos, steps), "L"
    if curr_dir == "U":
        if target_dir == "R":
            return walk_up(current_pos, steps), "R"
        else:
            return walk_up(current_pos, steps), "L"
    if curr_dir == "L":
        if target_dir == "L":
            return walk_left(current_pos, steps), "D"
        else:
            return walk_left(current_pos, steps), "U"
    else:
        return (0, 0), "P"


pos = [0, find_first_one(0), "R"]
current_pos = (pos[0], pos[1])
current_dir = pos[2]
last_dir = ""
for i in range(len(numbas)):
    if i < len(dirs):
        current_pos, current_dir = walk(
            current_pos, current_dir, numbas[i], dirs[i])
        last_dir = current_dir
    else:
        current_pos, current_dir = walk(
            current_pos, current_dir, numbas[i], dirs[i-1])

assert current_pos is not None
current_pos = tuple(x + 1 for x in current_pos)

facing = {"R": 0, "D": 1, "L": 2, "U": 3}[last_dir]

final_password = 1000*current_pos[0] + 4 * current_pos[1] + facing
print("Final password:", final_password)
