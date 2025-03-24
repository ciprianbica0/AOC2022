file = open('day20\\day20_input.txt', 'r')

seq = []
count1 = 0
for line in file:
    seq.append([int(line), count1])
    count1 += 1
# print(seq)

mixed = seq.copy()
l = len(mixed)
done = []
for i, done in seq:
    l = len(mixed)
    index1 = mixed.index([i, done])
    elem = mixed[index1]
    mixed.remove(elem)
    flag = 0
    if i >= l:
        l -= 1
        i = (i % l)
        flag = 1
    if i <= -l:
        l -= 1
        i = (i % l)
        flag = 1
    if i != 0:
        if not flag:
            l -= 1
        pos = (index1+i) % l
    else:
        pos = index1
    mixed.insert(pos, elem)
    # print(elem[0], "moved to", pos)
    # niceversion = [x[0] for x in mixed]
    # print(niceversion)

l = len(mixed)

# print(mixed)
index0 = next(i for i, x in enumerate(mixed) if x[0] == 0)
print(mixed[(1000+index0) % l][0] + mixed[(2000+index0) %
      l][0] + mixed[(3000+index0) % l][0])
