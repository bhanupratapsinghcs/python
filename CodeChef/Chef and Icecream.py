t = int(input())
for x in range(t):
    n = int(input())
    ls = list(map(int, input().split()))
    f, t = 0, 0
    sm = 0
    for i in ls:
        if i == 5:
            sm += i
            f += 1
        elif i == 10:
            t += 1
            if f >= 1:
                sm += 5
                f -= 1
            else:
                print("NO")
                break
        elif i == 15:
            if t >= 1:
                sm += 5
                t -= 1
            elif f >= 2:
                sm += 5
                f -= 2
            else:
                print("NO")
                break
    if sm == (n * 5):
        print("YES")
