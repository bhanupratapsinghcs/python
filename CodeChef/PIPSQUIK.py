t = int(input())
for i in range(t):
    n, h, y1, y2, l = map(int, input().split())
    a = 0
    # l -= 1
    for j in range(n):
        c, x = map(int, input().split())
        if c == 1:
            if (h - y1) <= x:
                a += 1
            elif l != 0:
                l -= 1
                if l == 0:
                    break
                a += 1
        else:
            if x <= y2:
                a += 1
            elif l != 0:
                l -= 1
                if l == 0:
                    break
                a += 1

    print(a)
# 2 2
# 2 1
# 1 10
# 2 8
# 2 4
# 1 2
