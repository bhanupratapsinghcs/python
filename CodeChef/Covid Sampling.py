t = int(input())
for x in range(t):
    n, p = map(int, input().split())
    print(1, 1, 1, n, n)
    i = 1
    z = int(input())
    if z == -1:
        break
    else:
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                if (n**2) - i < z:
                    print(1, end=" ")
                else:
                    print(0, end=" ")
                i += 1
            print("")
    z = int(input())
    if z == -1:
        break
    else:
        continue
