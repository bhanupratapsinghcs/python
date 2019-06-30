from itertools import combinations

n = int(input())
lst = list(input().split())
k = int(input())
combination_lst = list(combinations(lst, k))
ctr = 0
for i in combination_lst:
    if "a" in i:
        ctr += 1
print(f"{(ctr / len(combination_lst)):.4}")
