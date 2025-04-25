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


def calc(p1, symbol, p2):
    if symbol == '+':
        return p1 + p2
    if symbol == '-':
        return p1 - p2
    if symbol == '*':
        return p1 * p2
    if symbol == '/':
        return p1 / p2


def find_parts(monkeys):
    root = monkeys['root']
    part1 = root[0]
    part2 = root[2]
    q = [part1, part2]
    lst = []
    while len(q) > 0:
        curr = q[-1]
        v = monkeys[curr]
        if curr == "humn":
            monkeys[curr] = "humn"
        if not isinstance(v, Number):
            p1 = v[0]
            p2 = v[2]
            s = v[1]
            if p1 == "humn" or p2 == "humn" or p1 in lst or p2 in lst:
                lst.append(curr)
                q.remove(curr)

            else:
                if isinstance(monkeys[p1], Number) and isinstance(monkeys[p2], Number):
                    monkeys[curr] = calc(monkeys[p1], s, monkeys[p2])
                    q.remove(curr)
                    # fix_monkeys(monkeys)
                    continue

                if isinstance(monkeys[p1], Number):
                    p1 = monkeys[p1]
                else:
                    q.append(p1)
                if isinstance(monkeys[p2], Number):
                    p2 = monkeys[p2]
                else:
                    q.append(p2)
    fix_monkeys(monkeys)
    return (monkeys[part1], monkeys[part2], lst)
    # return calc(monkeys[part1], symb, monkeys[part2])


def fix_monkeys(monkeys):
    for key in monkeys.keys():
        if isinstance(monkeys[key], list):
            p1 = monkeys[key][0]
            s = monkeys[key][1]
            p2 = monkeys[key][2]

            if isinstance(monkeys[p1], Number) and isinstance(monkeys[p2], Number):
                monkeys[key] = calc(monkeys[p1], s, monkeys[p2])


p1, p2, q = find_parts(monkeys)
parts = []
numba = 0
if isinstance(p1, Number):
    numba = p1
    parts = p2
else:
    numba = p2
    parts = p1


def find_x(p, s, x, r, x_is_left):
    if s == "+":
        return r - p
    if s == "*":
        return r / p
    if x_is_left == 1:
        if s == "-":
            return r + p
        if s == "/":
            return p*r
    else:
        if s == "-":
            return p - r
        if s == "/":
            return p/r


def find_humn(parts, numba, monkeys):
    if not isinstance(parts, list):
        parts = monkeys[parts]
    x = 0
    p = 0
    left = 0
    p1 = parts[0]
    s = parts[1]
    p2 = parts[2]
    # print(p1, s, p2, '=', numba)
    if p1 == "humn":
        fix_monkeys(monkeys)
        return [find_x(monkeys[p2], s, p1, numba, 1)]
    if p2 == "humn":
        fix_monkeys(monkeys)
        return [find_x(monkeys[p1], s, x, numba, 0)]

    if isinstance(monkeys[p1], Number):
        x = p2
        p = monkeys[p1]
    else:
        x = p1
        p = monkeys[p2]
        left = 1
    if isinstance(p1, Number):
        x = p2
        p = p1
    if isinstance(p2, Number):
        x = p1
        p = p2
        left = 1
    # print(p, s, x, '=', numba)
    numba = find_x(p, s, x, numba, left)
    return x, numba


l = find_humn(parts, numba, monkeys)
while len(l) != 1:
    l = find_humn(l[0], l[1], monkeys)

print(int(l[0]))  # type:ignore
