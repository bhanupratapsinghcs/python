from math import ceil
t = int(input())
for x in range(t):
    a, b = map(int, input().split())
    print((ceil(a / 2) * ceil(b / 2)) + ((a // 2) * (b // 2)))
