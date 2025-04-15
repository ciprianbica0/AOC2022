from numbers import Number

file = open('day21\\day21_input.txt', 'r')

monkeys = {}
for line in file:
    line = line.split()
    line[0] = line[0][:4]
    if len(line[1:]) == 1 and line[1].isdigit():
        numba = int(line[1])
        monkeys[line[0]] = numba
    else:
        monkeys[line[0]] = line[1:]
    # print(line)
# print(monkeys)


def calc(p1, symbol, p2):
    if symbol == '+':
        return p1 + p2
    if symbol == '-':
        return p1 - p2
    if symbol == '*':
        return p1 * p2
    if symbol == '/':
        return p1 / p2


def find_root(monkeys):
    root = monkeys['root']
    part1 = root[0]
    symb = root[1]
    part2 = root[2]
    q = [part1, part2]

    while len(q) > 0:
        curr = q[-1]
        if curr == "humn":
            break
        v = monkeys[curr]
        if not isinstance(v, Number):
            p1 = v[0]
            p2 = v[2]
            s = v[1]
            if isinstance(monkeys[p1], Number) and isinstance(monkeys[p2], Number):
                monkeys[curr] = calc(monkeys[p1], s, monkeys[p2])
                q.remove(curr)
                continue
            if isinstance(monkeys[p1], Number):
                p1 = monkeys[p1]
            else:
                q.append(p1)
            if isinstance(monkeys[p2], Number):
                p2 = monkeys[p2]
            else:
                q.append(p2)
    print(monkeys[part1], monkeys[part2])
    # return calc(monkeys[part1], symb, monkeys[part2])


print(find_root(monkeys))
