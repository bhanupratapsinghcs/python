t = int(input())
for i in range(t):
    n = int(input())
    q = list(map(int, input().split()))
    cnt = 0
    if n == 1:
        print("Case #" + str(i) + ":" + " " + str(cnt))
    elif n < 3:
        if q[1] > q[0] or q[0] > q[1]:
            print("Case #" + str(i) + ":" + " " + str(cnt))
        else:
            print("Case #" + str(i) + ":" + " " + str(cnt))
    else:
        for j in range(1, n - 1):
            if q[j] > q[j - 1] and q[j + 1] < q[j]:
                cnt += 1
        print("Case #" + str(i) + ":" + " " + str(cnt))
