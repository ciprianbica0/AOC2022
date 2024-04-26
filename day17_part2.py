import time
import numpy

f = open("day17_input.txt", "r")
t1 = time.time()

# SETUP
room = numpy.zeros((35000, 7), numpy.int32)
# print(room, '\n')
jet_streams = f.read()

# print(len(jet_streams))

rock1 = numpy.zeros((1, 4))
for i in range(len(rock1[0])):
    rock1[0][i] = 1
# print(rock1, '\n')

rock2 = numpy.zeros((3, 3))
for i in range(len(rock2[1])):
    rock2[i][1] = 1
    rock2[1][i] = 1
# print(rock2, '\n')

rock3 = numpy.zeros((3, 3))
for i in range(len(rock3[1])):
    rock3[i][2] = 1
    rock3[2][i] = 1
# print(rock3, '\n')

rock4 = numpy.zeros((4, 1))
for i in range(4):
    rock4[i][0] = 1
# print(rock4, '\n')

rock5 = numpy.zeros((2, 2))
for i in range(2):
    for j in range(2):
        rock5[i][j] = 1

# print(rock5, '\n')
rocks = [rock1, rock2, rock3, rock4, rock5]
# ________________________________________________________________________________________________________________________
rockcounter = 0
jets = 0
h = 0


def getSpawnLocation():
    global rockcounter, h
    return (room.shape[0]-h-4, 2)


def spawnRock():
    global rockcounter
    coord = []
    botlefcor = getSpawnLocation()
    rock = rocks[rockcounter % 5]
    for i in range(rock.shape[0], 0, -1):
        for j in range(rock.shape[1]):
            if rock[i-1][j] == 1:
                coord.append([botlefcor[0]-(rock.shape[0]-i), botlefcor[1]+j])
    return coord


def rock_fall(coord):
    global room
    global jets
    global jet_streams
    global h
    stopped = False
    while not stopped:
        dir = -1
        if jet_streams[jets % len(jet_streams)] == ">":
            dir = 1
        jets += 1
        blocked = False
        for i in coord:
            if blocked:
                break
            if i[1]+dir not in range(room.shape[1]):
                blocked = True
            if not blocked:
                if room[i[0]][i[1]+dir] == 1:
                    blocked = True
        if not blocked:
            for i in coord:
                i[1] += dir
        stopped = False
        for i in coord:
            if stopped:
                break
            if i[0]+1 not in range(room.shape[0]):
                stopped = True
            if not stopped:
                if room[i[0]+1][i[1]] == 1:
                    stopped = True
        if not stopped:
            for i in coord:
                i[0] += 1
        else:
            for i in coord:
                room[i[0]][i[1]] = 1
    for (i, j) in coord:
        if i <= room.shape[0] - h:
            h = room.shape[0] - i


def printroom():
    for i in range(room.shape[0]):
        for j in range(room.shape[1]):
            print(room[i][j], end=" ")
        print()


def simulate():
    diffs = []
    global rockcounter
    global h
    while rockcounter < 20000:
        a = h
        rock_fall(spawnRock())
        diffs.append(h-a)
        rockcounter += 1
    return diffs


def find_cycle_length(list1):
    """Given the list of height deltas finds the cycle length
    """
    sample = list1[10000:11000]
    a = 0
    b = 0

    current = []
    c = -1

    for i in range(len(list1)):
        current.append(list1[i])
        if len(current) < len(sample):
            continue
        useful = current[-len(sample):]
        if useful == sample:
            if c > 0 and a == 0:
                a = i
                c += 1
                continue
            if a != 0 and b == 0:
                b = i
                return b-a
            c += 1
    return c


def find_unique(cl, list1):
    """Given the list of height deltas and the cycle length,
      finds the index where the unique sequence stops
    """
    result = 0
    c = -1
    while c <= 0:
        looking_for = list1[result:cl+result]
        looking_for_sum = sum(looking_for)
        c = -1
        current = []
        for i in range(len(list1)):
            current.append(list1[i])

            if len(current) < len(looking_for):
                continue

            useful = current[-len(looking_for):]
            if useful == looking_for and sum(useful) == looking_for_sum:
                c += 1
        result += 1
    return result-1


diffs = simulate()

cyclelen = find_cycle_length(diffs)
print("Length of cycle = ", cyclelen)

unique1 = find_unique(cyclelen, diffs)
print("Cycling starts from", unique1)
firstunique = sum(diffs[:unique1])
print("Sum of unique seq", firstunique)
cyclesum = sum(diffs[unique1:unique1+cyclelen])
firstcycle = diffs[unique1:unique1+cyclelen]
print("Cyclesum = ", cyclesum)
tcf = (1000000000000-unique1)//cyclelen
print("Times cycle fits in 1 trillion =", tcf)
leftover = sum(firstcycle[:((1000000000000-unique1) % cyclelen)])
print("Leftover =", (1000000000000-unique1) % cyclelen)
print("__________________________________________________________________")
print("Final sum =", firstunique + cyclesum * tcf + leftover)


t2 = time.time()
print("\n""Duration", t2-t1, "~=", "%0.2f" % ((t2-t1)/60), "minutes")
