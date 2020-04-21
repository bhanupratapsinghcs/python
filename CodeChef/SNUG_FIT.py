t = int(input())
for x in range(t):
    n = int(input())
    cnt = 0
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    at = sorted(a)
    bt = sorted(b)
    for i in range(n):
        if at[i] > bt[i]:
            cnt += bt[i]
        else:
            cnt += at[i]
    print(cnt)
# solved
