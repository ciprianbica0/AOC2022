import time

f = open("day15_input.txt", "r")
sensors = []
beacons = []
explored = set()

t1 = time.time()
def mark_circle(sensor, beacon):
    # returns a set with a circle around the sensor, taking the beacon as a radius
    distance = abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])
    circle = set()
    todo = []
    todo.append((beacon[0], beacon[1]))
    while len(todo) != 0:
        v = todo.pop(0)
        neighbors = []
        for dx, dy in [(1, 1), (-1, -1), (-1, 1), (1, -1)]:  # GENIUS!!!!!!
            new_x, new_y = v[0] + dx, v[1] + dy
            neighbors.append((new_x, new_y))
        for w in neighbors:
            distance1 = abs(sensor[0]-w[0]) + abs(sensor[1]-w[1])
            if distance1 == distance and w not in circle:
                circle.add(w)
                todo.append(w)
        # print(len(circle))
    return circle

def in_circle (circle):
    result = []
    for x,y in circle:
        if y == target_row:
            result.append((x,y))
            print(x,y)
    result = sorted(result)
    if len(result)>1:
        start = result[0]
        end = result[1]
        for i in range(start[0],end[0]+1):
            if (i,target_row) not in beacons:
                explored.add(i)


for line in f:
    line = line.split()
    x = int(line[2].split("=")[1][:-1])
    y = int(line[3].split("=")[1][:-1])
    sensors.append((x, y))
    x = int(line[8].split("=")[1][:-1])
    y = int(line[9].split("=")[1])
    beacons.append((x, y))
# target_row = 10
target_row = 2000000
i = 0
for x1, y1 in sensors:
    x2, y2 = beacons[i]
    print("Sensor at x =", x1, ", y =", y1, ",beacon at x =", x2, ", y =", y2)
    i += 1
    distance = abs(x1-x2) + abs(y1-y2)
    print(distance)
    if target_row in range(y1, y1 + distance + 2) or target_row in range(y1, y1 - distance - 2, -1):
        print("Distance", distance)
        circle = mark_circle((x1, y1), (x2, y2))
        in_circle(circle)

print(len(explored))

t2 = time.time()
print("Duration", t2-t1)
# print(explored)