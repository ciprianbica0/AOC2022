import numpy as np
import copy

file = open('day23\\day23_input.txt', 'r')
rows, cols = 0, 0
elf_rows = []
c = 0
dirs1 = ['n', 's', 'w', 'e']

for line in file:
    row = []
    rows += 1
    cols = len(line)
    for i in range(len(line)):
        if line[i] == '#':
            row.append(i)
    elf_rows.append(row)

rows = rows + 2000
cols = cols + 2000

grid = np.zeros((rows, cols), dtype=int)

c_elves = []
for i in range(len(elf_rows)):
    for e in elf_rows[i]:
        grid[i + 1000, e+1000] = 1
        c_elves.append((i+1000, e+1000))


def adj_finder(matrix, position):
    adj = []

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            rangeX = range(0, matrix.shape[0])  # X bounds
            rangeY = range(0, matrix.shape[1])  # Y bounds

            (newX, newY) = (position[0]+dx, position[1]+dy)  # adjacent cell

            if (newX in rangeX) and (newY in rangeY) and (dx, dy) != (0, 0):
                adj.append((newX, newY))

    return adj


elves = {}
for x, y in c_elves:
    elves[(x, y)] = copy.copy(dirs1)


def will_move(x, y):
    neighbors = set(adj_finder(grid, (x, y)))
    if neighbors.intersection(set(elves.keys())):
        return 1
    else:
        return 0


def north_free(elf, elves):
    x = elf[0]
    y = elf[1]
    if x-1 >= 0:
        possibilities = ((x-1, y), (x-1, y-1), (x-1, y+1))
        if not set(possibilities).intersection(set(elves.keys())):
            return 1
        return 0
    return 0


def south_free(elf, elves):
    x = elf[0]
    y = elf[1]
    if x+1 <= rows-1:
        possibilities = ((x+1, y), (x+1, y-1), (x+1, y+1))
        if not set(possibilities).intersection(set(elves.keys())):
            return 1
        return 0
    return 0


def west_free(elf, elves):
    x = elf[0]
    y = elf[1]
    if y-1 >= 0:
        possibilities = ((x, y-1), (x+1, y-1), (x-1, y-1))
        if not set(possibilities).intersection(set(elves.keys())):
            return 1
        return 0
    return 0


def east_free(elf, elves):
    x = elf[0]
    y = elf[1]
    if y+1 <= cols-1:
        possibilities = ((x, y+1), (x+1, y+1), (x-1, y+1))
        if not set(possibilities).intersection(set(elves.keys())):
            return 1
        return 0
    return 0


for _ in range(10):
    propositions = {}
    for (x, y), dirs in elves.items():
        if will_move(x, y):
            if not north_free((x, y), elves) and not south_free((x, y), elves) and not west_free((x, y), elves) and not east_free((x, y), elves):
                dirs.append(dirs.pop(0))
                elves[(x, y)] = dirs
                continue
            else:
                for letter in dirs:
                    if letter == 'n':
                        if north_free((x, y), elves):
                            dirs.append(dirs.pop(0))
                            elves[(x, y)] = dirs
                            propositions[(x, y)] = (x-1, y)
                            break
                    elif letter == 's':
                        if south_free((x, y), elves):
                            dirs.append(dirs.pop(0))
                            elves[(x, y)] = dirs
                            propositions[(x, y)] = (x+1, y)
                            break
                    elif letter == 'w':
                        if west_free((x, y), elves):
                            dirs.append(dirs.pop(0))
                            elves[(x, y)] = dirs
                            propositions[(x, y)] = (x, y-1)
                            break
                    elif letter == 'e':
                        if east_free((x, y), elves):
                            dirs.append(dirs.pop(0))
                            elves[(x, y)] = dirs
                            propositions[(x, y)] = (x, y+1)
                            break
        else:
            dirs.append(dirs.pop(0))
            elves[(x, y)] = dirs
    if not propositions:
        print("breaking at round", _+1)
        break
    not_move = []
    for elf1, spot1 in propositions.items():
        for elf2, spot2 in propositions.items():
            if elf1 != elf2 and spot1 == spot2:
                not_move.append(elf1)
                not_move.append(elf2)
    to_move = set(propositions.keys()).difference(set(not_move))
    for (x, y) in to_move:
        elves[(propositions[(x, y)])] = elves.pop((x, y))
    print("round", _+1)

max_row = max([x[0] for x in elves.keys()])
min_row = min([x[0] for x in elves.keys()])
min_col = min([x[1] for x in elves.keys()])
max_col = max([x[1] for x in elves.keys()])

# for r in range(min_row-1, max_row + 1):
#     print("".join('#' if (r, c) in elves else '.' for c in range(min_col-1, max_col + 2)))
# print()

print((max_row-min_row + 1)*(max_col-min_col+1)-len(elves.keys()))
