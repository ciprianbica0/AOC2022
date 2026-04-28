import numpy as np
import datetime
from collections import deque

strt = datetime.datetime.now()
file = open('day24\\day24_input.txt', 'r')
c1 = 0
r = 0
for line in file:
    c1 = len(line)
    r += 1
r -= 2
c1 -= 2
print(r, c1)
valley = np.zeros((r, c1))
blizzards = []
line_num = -2
file = open('day24\\day24_input.txt', 'r')
for line in file:
    line_num += 1
    for c in range(len(line)):
        if line[c] == '^':
            blizzards.append([(line_num, c-1), "U"])
        if line[c] == '>':
            blizzards.append([(line_num, c-1), "R"])
        if line[c] == '<':
            blizzards.append([(line_num, c-1), "L"])
        if line[c] == 'v':
            blizzards.append([(line_num, c-1), "D"])


def advance_time(bs, rows, cols):
    result = []
    for coords, direction in bs:
        new_coords = (0, 0)
        if direction == "U":
            if coords[0] == 0:
                new_coords = (rows-1, coords[1])
            else:
                new_coords = (coords[0]-1, coords[1])
        elif direction == "D":
            if coords[0] == rows-1:
                new_coords = (0, coords[1])
            else:
                new_coords = (coords[0]+1, coords[1])
        elif direction == "R":
            if coords[1] == cols-1:
                new_coords = (coords[0], 0)
            else:
                new_coords = (coords[0], coords[1]+1)
        elif direction == "L":
            if coords[1] == 0:
                new_coords = (coords[0], cols-1)
            else:
                new_coords = (coords[0], coords[1]-1)
        result.append([new_coords, direction])
    return result


blizzard_states = []


def compute_blizzard_states(bs):
    result = []
    seen = set()

    while True:
        key = tuple((tuple(c), d) for c, d in bs)
        if key in seen:
            break
        seen.add(key)

        positions = set(c for c, _ in bs)
        result.append(positions)

        bs = advance_time(bs, r, c1)

    return result


blizzard_states = compute_blizzard_states(blizzards)
print(len(blizzard_states))
position1 = (-1, 0)
position2 = (r, c1-1)

def bfs(bs, rows, cols, start_pos, goal, time):
    Q = deque()
    Q.append([start_pos, time])

    cycle = len(blizzard_states)

    visited = set()
    visited.add((start_pos[0], start_pos[1], time % cycle))

    while Q:
        v = Q.popleft()
        position = v[0]

        if v[0] == goal:
            return v
        else:
            possibilities = [
                (position[0]+1, position[1]),
                (position[0], position[1]+1),
                (position[0]-1, position[1]),
                (position[0], position[1]-1),
                position
            ]

            bzds_next = blizzard_states[(v[1]+1) % len(blizzard_states)]
            bzds_next_loc = bzds_next

            for x, y in possibilities:
                state = ((x, y), (v[1]+1) % cycle)
                if (
                    (0 <= x <= rows-1 and 0 <= y <= cols-1) or
                    (x, y) == start_pos or
                    (x, y) == goal
                ):
                    if (x, y) not in bzds_next_loc and state not in visited:
                        visited.add(state)
                        Q.append([(x, y), v[1]+1])

    return [0, 0]


result1 = bfs(blizzards, r, c1, position1, position2, 0)
result2 = bfs(blizzards, r, c1, position2, position1, result1[1])
result3 = bfs(blizzards, r, c1, position1, position2, result2[1])

print(result3[1], "steps")
end = datetime.datetime.now()
print("ended in", end-strt)