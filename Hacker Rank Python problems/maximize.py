# # maxamize it
# 3 1000
# 2 5 4
# 3 7 8 9
# 5 5 7 8 9 10

# name, *line = input().split()
# scores = list(map(float, line))

# x, y = map(int, raw_input().split()) input in one line


import itertools

k, m = map(int, input().strip().split(' '))
a = []
for i in range(k):
    t = list(map(int, input().split()))
    a.append(t)

# print(a)

mx = 0
for tp in itertools.product(*a):
    print(tp)
    res = sum([x**2 for x in tp]) % m
    print(res)
    if res > mx:
        mx = res

print(mx)
