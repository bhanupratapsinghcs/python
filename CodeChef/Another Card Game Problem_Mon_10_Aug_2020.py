from math import ceil
t = int(input())
for x in range(t):
    c, r = map(int, input().split())
    c = ceil(c / 9)
    r = ceil(r / 9)
    if c > r:
        print(1, r)
    elif r > c:
        print(0, c)
    else:
        print(1, r)
