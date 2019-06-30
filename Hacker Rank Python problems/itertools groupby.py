from itertools import groupby


# print(*[(len(list(c)), int(k)) for k, c in groupby(input())])

for k, g in groupby(input()):
    print("({}, {})".format(len(list(g)), k), end=" ")
