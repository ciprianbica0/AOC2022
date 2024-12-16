from math import floor
import numpy as np
f = open("day10\\day10_input.txt", "r")

cycle = 0
X = 1
screen = []
for i in range(0, 6):
    row = []
    for j in range(0, 40):
        row.append(".")
    screen.append(row)

screen = np.array(screen)


def drawpixel():
    print(cycle)
    if cycle % 40 == X-1 or cycle % 40 == X or cycle % 40 == X+1:
        screen[int(cycle/40)][cycle % 40] = "#"


for line in f:
    line = line.split()
    command = line[0]
    drawpixel()
    if command == "noop":
        cycle += 1
        continue
    if command == "addx":
        par = int(line[1])
        cycle += 1
        drawpixel()
        X += par
        cycle += 1
        continue

for i in range(0, 6):
    for j in range(0, 40):
        print(screen[i][j], end=" ")
    print()
