def power(s):
    sm = 0
    for i in range(len(s)):
        sm += int(s[i])
    return sm


t = int(input())
for x in range(t):
    n = int(input())
    c, m = 0, 0
    for i in range(n):
        a, b = map(str, input().split())
        # A,B=0,0
        A = power(a)
        B = power(b)
        if A > B:
            c += 1
        elif A < B:
            m += 1
        elif A == B:
            c += 1
            m += 1
    if c > m:
        print('0', c)
    elif c < m:
        print('1', m)
    else:
        print('2', c)
