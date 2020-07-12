t = int(input())
for x in range(t):
    n, m = map(int, input().split())
    ls = list(map(int, input().split()))
    if sum(ls) < m:
        print(sum(ls))
    else:
        print(m)
