f = open("day10\\day10_input.txt", "r")

cycle = 1
reg = 1
total_sum = 0


def drawpixel():
    global total_sum
    if cycle == 20 or (cycle-20) % 40 == 0:
        total_sum += cycle*reg
        print(cycle, reg)
    if cycle == 220:
        print("total sum at 220 is ", total_sum)
    return total_sum


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
        reg += par
        cycle += 1
        continue

print(total_sum)
