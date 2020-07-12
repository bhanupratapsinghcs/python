t = int(input())
for x in range(t):
    n, k = map(int, input().split())
    ls = list(map(int, input().split()))
    sm = 0
    for i in ls:
        if i > k:
            i = k
        sm += i
    print(sum(ls) - sm)
