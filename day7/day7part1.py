# import math
# import string
# class Folder:
#     def __init__(self,parent):
#         self.children = []
#     def add_child(self, obj):
#         self.children.append(obj)

# foldertosize = {}
# ftc = {}
# parentmap = {}
# wd = "/"
# folderlist = []



# for line in data:
#     if (line.startswith("$ cd ")) and line.split().pop() != "..":
#         foldertosize[line.split().pop()] = 0

# for line in data:
#     start = line.split()[0]
#     if line.startswith("$ cd"):
#         name = line.split().pop()
#         print(name)
#         wd = name
#     elif line.startswith("dir "):
#         name1 = line.split().pop()
#         folderlist.append(name1)
#         ftc[wd] = folderlist
#     elif line[0] in string.digits:
#         foldertosize[wd] += int(line.split()[0])

# def getSize(name):
#     result = 0
#     if name in ftc.keys():
#         if len(ftc[name])>0:
#             for child in ftc[name]:
#                 result += getSize(child)
#     else:
#         result += foldertosize[name]
#     return result

# for key in ftc.keys():
#     for child in ftc[key]:
#         parentmap[child] = key

# for line in data:
#     if line.startswith("$ cd"):
#         name = line.split().pop()
#         if name != "..":
#             wd = name
#         # else:
#             # wd = parentmap[wd]
# print(ftc)
# print(parentmap)

# for key in ftc.keys():
#     for child in ftc[key]:
#         foldertosize[key] += getSize(child)



# result = 0
# for key in foldertosize.keys():
#     if foldertosize[key] <= 100000:
#         result += foldertosize[key]
# print(result)

from collections import defaultdict

f = open("AoC2022/Day7/day7.txt", "r")
data = f.readlines()

with open("AoC2022/Day7/day7.txt") as f:
    commands = f.readlines()

sizes = defaultdict(int)
stack = []

for c in commands:
    if c.startswith("$ ls") or c.startswith("dir"):
        continue
    if c.startswith("$ cd"):
        dest = c.split()[2]
        if dest == "..":
            stack.pop()
        else:
            path = f"{stack[-1]}_{dest}" if stack else dest
            stack.append(path)
    else:
        size, file = c.split()
        for path in stack:
            sizes[path] += int(size)

needed_size = 30000000 - (70000000 - sizes["/"])
for size in sorted(sizes.values()):
    if size > needed_size:
        break

print(sum(n for n in sizes.values() if n <= 100000)) # task 1
print(size) # task 2
