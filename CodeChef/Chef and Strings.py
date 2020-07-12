t = int(input())
for x in range(t):
    n = int(input())
    ls = list(map(int, input().split()))
    sm = 0
    for i in range(n - 1):
        t = (abs(ls[i + 1] - ls[i])) - 1
        sm += t
    print(sm)
