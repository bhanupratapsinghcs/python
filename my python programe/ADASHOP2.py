t = int(input())
for i in range(t):
    r, c = map(int, input().split())
    rt = 8 - r
    ct = 8 - c
    print(rt, ct)
    ls = []
    cnt = 0
    while rt != r and ct != c:
        if r + c == rt + c and (8 - rt) != r and (8 - ct) != c:
            rt = 8 - r
            ct = 8 - c
            r = rt
            c = ct
            print(rt, ct)
        else:
            rt = (rt + 8) % 7
            ct = (ct + 8) % 7
            r = rt
            c = ct
            print(rt, ct)
        cnt += 1
    print(cnt)
