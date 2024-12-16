import regex as re

f = open("day11\\day11_input.txt", "r")

monkeys = []
inspects = []
lines = []
for line in f:
    lines.append(line)


class monkey:
    def __init__(self, number, items, op, divisor, monkeys):
        self.number = number
        self.items = items
        self.behavior = op
        self.divisor = divisor
        self.monkeys = monkeys

    def inspect(self, current_item):
        operand1 = self.behavior[0]
        operation = self.behavior[1]
        operand2 = self.behavior[2]
        if operand1 == "old":
            operand1 = current_item
        if operand2 == "old":
            operand2 = current_item
        else:
            operand2 = int(operand2)

        if operation == "+":
            return operand1 + operand2
        if operation == "*":
            return operand1 * operand2

    def __str__(self):
        return f"Monkey: {self.number}, Items: {self.items} ,Inspection: {self.behavior} ,Divisor {self.divisor} ,Other monkeys {self.monkeys}"


number = 0
items = []
operation = []
divisor = 0
choices = []
for i in range(0, len(lines)):
    number = int(i/7)
    line = lines[i].split()
    if len(line) == 0:
        continue

    if line[0] == "Starting":
        for item in line[2:]:
            item = re.sub(r"\D", "", item)
            items.append(int(item))
    if line[0] == "Operation:":
        operation = line[3:]
    if line[0] == "Test:":
        divisor = int(line[3])
    if line[1] == "true:":
        choices.append(int(line[-1]))
    if line[1] == "false:":
        choices.append(int(line[-1]))
        monkeys.append(monkey(number, items, operation, divisor, choices))
        number = 0
        items = []
        operation = []
        divisor = 0
        choices = []
for i in range(0, len(monkeys)):
    inspects.append(0)

for i in range(0, 20):
    for m in monkeys:
        while len(m.items) != 0:
            curr = m.items.pop(0)
            c = m.inspect(curr)
            inspects[m.number] += 1
            c = int(c/3)
            if c % m.divisor == 0:
                monkeys[m.monkeys[0]].items.append(c)
            else:
                monkeys[m.monkeys[1]].items.append(c)

print(sorted(inspects)[-1]*sorted(inspects)[-2])
