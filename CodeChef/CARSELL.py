t = int(input())
for i in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    s = sorted(p, reverse=True)
    sell = 0
    for x in range(n):
        if s[x] - x <= 0:
            break
        else:
            sell = sell + s[x] - x
    print(sell % 1000000007)
