from itertools import combinations
strg, n = input().split()
for i in range(1, int(n) + 1):
    lst = list(combinations(sorted(strg), i))
    [print("".join(x)) for x in lst]
