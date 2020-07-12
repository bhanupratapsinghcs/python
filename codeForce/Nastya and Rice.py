t = int(input())
for x in range(t):
    n, a, b, c, d = map(int, input().split())
    l = n * (a - b)
    r = n * (a + b)
    if r < (c - d) or (c + d) < l:
        print("No")
    else:
        print("Yes")
