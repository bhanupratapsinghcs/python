t = int(input())
for i in range(t):
    n = int(input())
    ls = list(map(int, input().split()))
    mx = 1
    mn = 10
    tmn = 0
    i = 1
    j = 0
    k = 0
    for x in range(n - 1):
        r = ls[x + 1] - ls[x]
        if r <= 2:
            j = 1
            i += 1
            k = 0
        if mx < i:
            mx = i
        if x == 0 and r > 2:
            tmn = 1
        if x == (n - 2) and r > 2:
            tmn = 1
        if k >= 1:
            tmn = 1
        if (r > 2 and i > 1) or x == (n - 2):
            if x == (n - 2) and j == 0:
                mn = 1
            if mn > i and i > 1:
                mn = i
        if r > 2:
            i = 1
            k += 1
    if tmn == 1:
        mn = 1
    print(mn, mx)
