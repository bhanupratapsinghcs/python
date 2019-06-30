from itertools import combinations_with_replacement
strg, n = input().split()
lst = list(combinations_with_replacement(sorted(strg), int(n)))
[print("".join(x)) for x in lst]
