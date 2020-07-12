t = int(input())
for x in range(t):
    p, q, r = map(int, input().split())
    a, b, c = map(int, input().split())
    mn = 3
    l = [[a - p, b - q, c - r], [a - p, b - r, c - q], [a - q, b - p, c - r], [a - q, b - r, c - p], [a - r, b - p, c - q], [a - r, b - q, c - p]]
    for i in l:
        s1 = set(i)
        s = len(s1)
        if i[0] == 0 and i[1] == 0 and i[2] == 0:
            mn = 0
            break
        elif 0 in (i):
            n = (i).count(0)
            if n == 2:
                mn = 1
            else:
                if s == 3:
                    if mn > 2:
                        mn = 2
                else:
                    if mn > 1:
                        mn = 1
        else:
            # s1
            if mn > s:
                mn = s
    print(mn)
