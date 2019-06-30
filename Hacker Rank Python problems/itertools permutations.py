from itertools import permutations
strg, n = input().split()
lst = list(permutations(sorted(strg), int(n)))
[print("".join(x)) for x in lst]

# print list(permutations(['1','2','3'],2))
# [('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]