from math import ceil
t = int(input())
for x in range(t):
    a, b, c, d = map(int, input().split())
    if b >= a:
        print(b)
        continue
    elif c <= d:
        print(-1)
        continue
    r = c - d
    e = a - b
    n = e / r
    print(b + (ceil(n) * c))
