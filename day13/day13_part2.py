import ast
f = open("day13\\day13_input.txt", "r")


def compare_packets(left, right):
    for c in range(min(len(left), len(right))):
        # print("Compare ",left[c]," and ",right[c])
        if type(left[c]) == int and type(right[c]) == int:
            if left[c] == right[c]:
                continue
            if left[c] < right[c]:
                # print("Left side is smaller, so inputs are in the right order")
                return 1
            if left[c] > right[c]:
                # print("Right side is smaller, so inputs are not in the right order")
                return 0
        if type(left[c]) == list and type(right[c]) == list:
            result = compare_packets(left[c], right[c])
            if result != None:
                return result
        if type(left[c]) == list and type(right[c]) == int:
            # print("Mixed types; convert right to ",[right[c]]," and retry comparison")
            result = compare_packets(left[c], [right[c]])
            if result != None:
                return result
        if type(left[c]) == int and type(right[c]) == list:
            # print("Mixed types; convert left to ",[left[c]]," and retry comparison")
            result = compare_packets([left[c]], right[c])
            if result != None:
                return result
    if len(left) == len(right):
        pass
    if len(left) > len(right):
        # print("Right side ran out of items, so inputs are in the right order")
        return 0
    if len(right) > len(left):
        # print("Left side ran out of items, so inputs are in the right order")
        return 1


L = []
correct = []
for line in f:
    if line != "\n":
        h = ast.literal_eval(line)
        L.append(h)

L.append([[2]])
L.append([[6]])
flag = True
while flag:
    flag = False
    for i in range(len(L)-1):
        if compare_packets(L[i], L[i+1]) == 0 or None:
            L[i], L[i+1] = L[i+1], L[i]
            flag = True
product = 1
for i in range(len(L)):
    if(L[i]==[[2]] or L[i]==[[6]]):
        product*=(i+1)
print(product)