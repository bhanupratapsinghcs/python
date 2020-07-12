t = int(input())
for x in range(t):
    n, a, b = map(int, input().split())
    print((('abcdefghijklmnopqrstuvwxyz'[:b]) * n)[:n])
