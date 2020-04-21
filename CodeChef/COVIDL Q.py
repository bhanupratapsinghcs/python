t = int(input())
for i in range(t):
    n = int(input())
    q = list(map(int, input().split()))
    cnt = q.count(1)
    inx = q.index(1)
    c = 0
    if cnt == 1:
        print("YES")
    else:
        a = inx + 1
        cnt -= 1
        while cnt != 0 and a < n:
            print(a)
            if q[a] is 0:
                c += 1
            elif q[a] is 1:
                cnt -= 1
                if c < 5:
                    print("NO")
                    break
                elif cnt == 0:
                    print("YES")
                c = 0
            a += 1
