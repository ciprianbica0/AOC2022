f = open("AoC2022/Day2/day2.txt", "r")
t = 0
score = 0
for line in f:
    elfchoice = line[:1]
    outcome = line[2:3]

    if elfchoice == 'A':
        if outcome == 'X':
            score += 3
        elif outcome == 'Y':
            score += 1+3
        elif outcome == 'Z':
            score += 2+6
    if elfchoice == 'B':
        if outcome == 'X':
            score += 1
        elif outcome == 'Y':
            score += 2+3
        elif outcome == 'Z':
            score += 3+6
    if elfchoice == 'C':
        if outcome == 'X':
            score += 2
        elif outcome == 'Y':
            score += 3+3
        elif outcome == 'Z':
            score += 1+6
print(score)
