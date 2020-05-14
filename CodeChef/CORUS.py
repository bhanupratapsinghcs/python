from sys import stdin
t = int(input())
for i in range(t):
    n, q = map(int, input().split())
    s = input()
    st = list(set(s))
    print(st)
    l = []
    for x in st:
        l.append(s.count(x))
    for j in range(q):
        c = int(input())
        mn = 0
        for x in l:
            if x > c:
                mn += (x - c)
        print(mn)
