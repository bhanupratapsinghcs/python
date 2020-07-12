t = int(input())
for x in range(t):
    n = int(input())
    ls = list(map(int, input().split()))
    s = set(ls)
    mn = 1000
    if len(s) < n:
        print(0)
        continue
    else:
        ls = sorted(ls)
        for i in range(n - 1):
            r = ls[i + 1] - ls[i]
            if mn > r:
                mn = r
        print(mn)
