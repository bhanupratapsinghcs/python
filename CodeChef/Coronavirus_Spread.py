t = int(input())
for i in range(t):
    n = int(input())
    ls = list(map(int, input().split()))
    q = []
    cnt = 1
    for x in range(n - 1):
        if ls[x + 1] - ls[x] <= 2:
            cnt += 1
        else:
            q.append(cnt)
            cnt = 1
    if cnt >= 1:
        q.append(cnt)
    print(min(q), max(q))
    # mx = 1
    # mn = 10
    # i = 0
    # j = 0
    # for x in range(n - 1):
    #     r = ls[x + 1] - ls[x]
    #     if r <= 2:
    #         j = 1
    #         i += 1
    #     if mx < i + 1:
    #         mx = i + 1
    #     if x == 0 and r > 2:
    #         mn = 1
    #     if (r > 2 and i > 0) or x == (n - 2):
    #         if x == (n - 2) and j == 0:
    #             mn = 1
    #         if mn > i + 1 and i > 0:
    #             mn = i + 1
    #     if r > 2:
    #         i = 0
    # print(mn, mx)
