t = int(input())
profit = 0
for z in range(t):

    n = int(input())
    l = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(n):
        m, r = input().split()
        q = 0
        if r == '12':
            q = 0
        elif r == '3':
            q = 1
        elif r == '6':
            q = 2
        else:
            q = 3
        l[ord(m) - 65][q] = l[ord(m) - 65][q] + 1
    s = []
    w = 0

    ls = 0
    for i in l:
        c = 0
        for k in i:
            if k != 0:
                c = c + 1
                break
        if c == 0:
            ls = ls + 1
    while(len(l) > 0):
        mx = 0
        for j in l:
            if mx < max(j):
                mx = max(j)
        d = []
        for i in range(len(l)):
            for j in range(len(l)):
                if(l[i][j] == mx):
                    d.append(i)
                    d.append(j)
        del l[d[0]]
        for k in l:
            del k[d[1]]
        s.append(mx)

    w = s[0] * 100 + s[1] * 75 + s[2] * 50 + s[3] * 25
    profit = profit + (w - ls * 100)
    print(w - ls * 100)
print(profit)


# solved