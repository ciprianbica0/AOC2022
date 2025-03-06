from time import time

s = time()

file = open('day19\\day19_input.txt', 'r')
lines = file.read

blueprints = []

for lines in file:
    lines = lines.split(" ")
    blueprints.append([lines[6], lines[12], lines[18],
                      lines[21], lines[27], lines[30]])

for blueprint in blueprints:
    blueprint = [int(item) for item in blueprint]
    ore_robot = int(blueprint[0])
    clay_robot = int(blueprint[1])
    obsidian_robot = (int(blueprint[2]), int(blueprint[3]))
    geode_robot = (int(blueprint[4]), int(blueprint[5]))


def start(blueprint):
    blueprint = [int(item) for item in blueprint]
    result = 0
    root = (24, (0, 0, 0, 0), (1, 0, 0, 0))
    result = bfs(blueprint, root)

    return result


counter = 0
max_depth = 0

states = set()


def bfs(blueprint, root):
    queue = []
    max1 = 0
    explored = set()
    explored.add(root)
    queue.append(root)
    while (len(queue) > 0):
        v = queue.pop()
        resources = v[1]
        timeleft = v[0]
        geodes = resources[3]
        if geodes > max1:
            max1 = geodes
        if timeleft == 0:
            continue
        potential = geodes + ((timeleft+1)*(timeleft+2))/2
        if potential < max1:
            continue
        robots = v[2]
        ore = resources[0]
        clay = resources[1]
        obsidian = resources[2]
        rob_geo = robots[3]
        rob_ore = robots[0]
        rob_clay = robots[1]
        rob_obs = robots[2]
        if timeleft > 1:
            if ore >= blueprint[4] and obsidian >= blueprint[5]:
                state = (timeleft-1, (ore-blueprint[4]+rob_ore, clay+rob_clay, obsidian-blueprint[5]+rob_obs,
                        geodes+rob_geo), (rob_ore, rob_clay, rob_obs, rob_geo+1))
                if state not in explored:
                    queue.append(state)
                    explored.add(state)
            if ore >= blueprint[2] and clay >= blueprint[3]:
                state = (timeleft-1, (ore-blueprint[2]+rob_ore, clay-blueprint[3]+rob_clay, obsidian+rob_obs,
                        geodes+rob_geo), (rob_ore, rob_clay, rob_obs+1, rob_geo))
                if state not in explored:
                    queue.append(state)
                    explored.add(state)
            if ore >= blueprint[1] and rob_clay < blueprint[3]:
                state = (timeleft-1, (ore-blueprint[1]+rob_ore, clay+rob_clay, obsidian+rob_obs,
                        geodes+rob_geo), (rob_ore, rob_clay+1, rob_obs, rob_geo))
                if state not in explored:
                    queue.append(state)
                    explored.add(state)
            if ore >= blueprint[0] and rob_ore < max(blueprint[0], blueprint[1]):
                state = (timeleft-1, (ore-blueprint[0]+rob_ore, clay+rob_clay, obsidian+rob_obs,
                        geodes+rob_geo), (rob_ore+1, rob_clay, rob_obs, rob_geo))
                if state not in explored:
                    queue.append(state)
                    explored.add(state)
        
        state = (timeleft-1, (ore+rob_ore, clay+rob_clay, obsidian+rob_obs,
                              geodes+rob_geo), (rob_ore, rob_clay, rob_obs, rob_geo))
        if state not in explored:
            queue.append(state)
            explored.add(state)
        explored.add(v)
    return max1


result = 0
for i in range(len(blueprints)):
    result += start(blueprints[i]) * (i+1)
print("Sum of quality levels: ", result)
e = time()
print("time = ", e-s)
