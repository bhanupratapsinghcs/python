t = int(input())
for x in range(t):
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    # print(p[::-1])
    an = -1
    for i in p[::-1]:
        if i < k:
            if k % i == 0:
                an = i
                break
    if an == -1:
        print(-1)
    else:
        print(an)
