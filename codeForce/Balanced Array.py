t = int(input())
for x in range(t):
    n = int(input())
    l = []
    if (n // 2) % 2 != 0:
        print("NO")
    else:
        print("YES")
        for j in range(1, n // 2 + 1):
            l.append(j * 2)
        r = 1
        for j in range(1, n // 2 + 1):
            l.append(r)
            r += 2
        l[n - 1] = r - 2 + (n // 2)
        for i in l:
            print(i, end=" ")
        print()
