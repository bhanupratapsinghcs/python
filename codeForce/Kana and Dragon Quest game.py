from math import floor
t = int(input())
for x in range(t):
    x, n, m = map(int, input().split())
    if (m * 10) >= x:
        print("YES")
        continue
    for i in range(n):
        x = floor(x / 2) + 10
    if (m * 10) >= x:
        print("YES")
        continue
    else:
        print("NO")
