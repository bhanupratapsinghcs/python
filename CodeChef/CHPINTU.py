t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    f = list(map(int, input().split()))
    p = list(map(int, input().split()))
    typef = set(f)
    ls = []
    for i in typef:
        mx = 0
        for j in range(n):
            if i == f[j]:
                mx += p[j]
        ls.append(mx)
    print(min(ls))
