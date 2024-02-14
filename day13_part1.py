import ast
f = open("day13_input.txt", "r")


def compare_packets(left, right):
    for c in range(min(len(left), len(right))):
        print("Compare ",left[c]," and ",right[c])
        if type(left[c]) == int and type(right[c]) == int:
            if left[c] == right[c]:
                continue
            if left[c] < right[c]:
                print("Left side is smaller, so inputs are in the right order")
                return 1
            if left[c] > right[c]:
                print("Right side is smaller, so inputs are not in the right order")
                return 0
        if type(left[c]) == list and type(right[c]) == list:
            result = compare_packets(left[c], right[c])
            if  result != None:
                return result
        if type(left[c]) == list and type(right[c]) == int:
            print("Mixed types; convert right to ",[right[c]]," and retry comparison")
            result = compare_packets(left[c], [right[c]])
            if  result != None:
                return result
        if type(left[c]) == int and type(right[c]) == list:
            print("Mixed types; convert left to ",[left[c]]," and retry comparison")
            result = compare_packets([left[c]], right[c])
            if  result != None:
                return result
    if len(left) == len(right):
        pass
    if len(left) > len(right):
        print("Right side ran out of items, so inputs are in the right order")
        return 0
    if len(right) > len(left):
        print("Left side ran out of items, so inputs are in the right order")
        return 1



L = []
correct = []
for line in f:
    if line != "\n":
        h = ast.literal_eval(line)
        L.append(h)

pair_counter = 1
for i in range(0, len(L), 2):
    f = L[i]
    s = L[i+1]
    if compare_packets(f, s):
        correct.append(pair_counter)
    pair_counter += 1
# print(correct)
print(sum(correct))
# print(type([])==list)
