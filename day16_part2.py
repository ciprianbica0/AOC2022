from copy import deepcopy
import time
import itertools
import numpy
f = open("day16_input.txt", "r")
t1 = time.time()
valves = []
distances = {}


class Valve:
    def __init__(self, name, pressure, neighbours, o):
        self.name = name
        self.pressure = pressure
        self.neighbours = neighbours
        self.open = o

    def __str__(self):
        return f"Valve: {self.name},Pressure {self.pressure}, Leads to {self.neighbours}, is open? {self.open}"


def checkpressure(total):
    toadd = 0
    for v in valves:
        if v.open == True:
            toadd += v.pressure
    total += toadd
    return total


def checkPressureopen(op, total):
    toadd = 0
    for i in op:
        v = findvalve(i)
        toadd += v.pressure
    return total+toadd


def closevalves():
    for v in valves:
        v.open = False


def findvalve(name):
    for i in valves:
        if i.name == name:
            return i
    return 0


def bfs(root):
    result = {}
    queue = []
    explored = []
    queue.append((root, 0))
    while len(queue) != 0:
        v, distance = queue.pop(0)
        result[v.name] = distance
        explored.append(v)
        for w in v.neighbours:
            w = findvalve(w)
            if w not in explored:
                queue.append((w, distance+1))
    return result


def calcMaxPressure1():
    result = 0
    queue = []
    bestpath = []
    explored = set()
    queue.append(([], useful, 26, 0))
    while len(queue) != 0:
        road, rest, tleft, pres = queue.pop(0)
        if pres > result:
            print(pres)
        result = max(result, pres)
        explored.add(tuple(road))
        for w in rest:
            if tuple(road+[w]) not in explored:
                c = deepcopy(rest)
                c.remove(w)
                l = road[-1] if len(road) > 0 else "AA"
                if tleft-distances[l][w]-1 <= 2:
                    m = pres+tleft*checkPressureopen(road, 0)
                    if result < m:
                        result = m
                        bestpath = road
                else:
                    queue.append((road+[w], c, tleft-distances[l][w]-1,
                                  (distances[l][w]+1)*checkPressureopen(road, 0)+pres))
    print(bestpath)
    return result, set(bestpath)


def calcMaxPressure2(to_avoid):
    result = 0
    queue = []
    bestpath = []
    explored = set()
    queue.append(([], useful, 26, 0))
    while len(queue) != 0:
        road, rest, tleft, pres = queue.pop(0)
        if pres > result:
            print(pres)
        result = max(result, pres)
        explored.add(tuple(road))
        for w in rest:
            if w not in to_avoid:
                if tuple(road+[w]) not in explored:
                    c = deepcopy(rest)
                    c.remove(w)
                    l = road[-1] if len(road) > 0 else "AA"
                    if tleft-distances[l][w]-1 <= 2:
                        m = pres+tleft*checkPressureopen(road, 0)
                        if result < m:
                            result = m
                            bestpath = road
                    else:
                        queue.append((road+[w], c, tleft-distances[l][w]-1,
                                      (distances[l][w]+1)*checkPressureopen(road, 0)+pres))
    print(bestpath)
    return result


def check_valve_order(arr):
    closevalves()
    total = 0
    curr = "AA"
    dest = arr.pop(0)
    d = distances[curr][dest]
    for _ in range(0, 30):
        total = checkpressure(total)
        if d == 0:
            v = findvalve(dest)
            if v != None:
                v.open = True
            curr = dest
            if len(arr) > 0:
                dest = arr.pop(0)
            d = distances[curr][dest]
        else:
            d -= 1
    return total


# SETUP
for line in f:
    line = line.split()
    name = line[1].split(",")[0]
    pressure = int((line[4].split("=")[1]).split(";")[0])
    neighbours = []
    for i in range(len(line) - 9):
        neighbour_name = line[9 + i].split(",")[0]
        neighbours.append(neighbour_name)
    v = Valve(name, pressure, neighbours, False)
    valves.append(v)

useful = []
for v in valves:
    distances[v.name] = bfs(v)
    if v.pressure > 0:
        useful.append(v.name)


max1 = 0
max_pressure1, to_avoid = calcMaxPressure1()
max_pressure2 = calcMaxPressure2(to_avoid)
print("Max pressure ", max_pressure1+max_pressure2)
# for i in reachable_permutations:
#     c = check_valve_order(list(i))
#     if c > max1:
#         max1 = c
#         print(list(i))
# print(check_valve_order(useful))
t2 = time.time()
print("Duration", t2-t1, "~=", "%0.2f" % ((t2-t1)/60), "minutes")
