t = int(input())
for x in range(t):
    n = int(input())
    n = (((n - 1) // 2))
    print(((n * (n + 1) * ((2 * n) + 1)) // 6) * 8)
