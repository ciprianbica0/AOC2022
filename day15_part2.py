from collections import defaultdict
import time

f = open("day15_input.txt", "r")
sensors = []
beacons = []
suspects = set()
real_suspects = set()
circles = defaultdict(dict)
t1 = time.time()
distances = {}
circle_counter = 0
last_counter = 0


def mark_circle(sensor, beacon, counter):
    global last_counter
    visited = set()
    # returns a set with a circle around the sensor, taking the beacon distance as a radius
    distance = abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])
    distances[sensor] = distance
    circle = set()
    todo = set()
    todo.add((beacon[0], beacon[1]))
    todo.add((beacon[0], beacon[1]+1))
    todo.add((beacon[0]+1, beacon[1]))
    todo.add((beacon[0]+1, beacon[1]+1))

    while len(todo) != 0:
        v = todo.pop()
        if v not in visited:
            visited.add(v)
            neighbors = []
            for dx, dy in [(1, 1), (-1, -1), (-1, 1), (1, -1)]:  # GENIUS!!!!!!
                new_x, new_y = v[0] + dx, v[1] + dy
                neighbors.append((new_x, new_y))
            for w in neighbors:
                distance1 = abs(sensor[0]-w[0]) + abs(sensor[1]-w[1])
                # if distance1 == distance and w not in circle:
                #     circle.add(w)
                #     todo.add(w)
                if distance1 == distance+1:
                    if 0 <= w[0] <= 4000000 and 0 <= w[1] <= 4000000:
                        if w in suspects and counter != last_counter:
                            real_suspects.add(w)
                        else:
                            suspects.add(w)
                        todo.add(w)
    last_counter = circle_counter
    return circle


def check_suspects():
    global real_suspects
    c = 0
    to_remove = set()
    for x1, y1 in real_suspects:
        for a, b in distances:
            d = abs(x1-a) + abs(y1-b)
            if d <= distances[(a, b)]:
                to_remove.add((x1, y1))
                break
        c += 1
        if c % 100000 == 0:
            print("worked through ", c, "suspects...")
    for x in to_remove:
        real_suspects.remove(x)


for line in f:
    line = line.split()
    x = int(line[2].split("=")[1][:-1])
    y = int(line[3].split("=")[1][:-1])
    sensors.append((x, y))
    x = int(line[8].split("=")[1][:-1])
    y = int(line[9].split("=")[1])
    beacons.append((x, y))

i = 0
for x1, y1 in sensors:
    x2, y2 = beacons[i]
    print("Sensor at x =", x1, ", y =", y1, ",beacon at x =", x2, ", y =", y2)
    i += 1
    distance = abs(x1-x2) + abs(y1-y2)
    print(distance)
    print("Distance", distance)
    circle = mark_circle((x1, y1), (x2, y2), circle_counter)
    print("Suspects", len(suspects))
    print("Real Suspects", len(real_suspects))
    circle_counter += 1
    # range_fill(circle,(x1, y1))
check_suspects()
# print(len(suspects))
# print(suspects)
print(real_suspects)
t2 = time.time()
print("Duration", t2-t1)
# {(3405562, 3246513)}
