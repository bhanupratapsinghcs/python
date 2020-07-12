t = int(input())
for x in range(t):
    n = int(input())
    X = {}
    Y = {}
    a, b = 0, 0
    for i in range(4 * n - 1):
        x, y = map(int, input().split())
        if x in X:
            X[x] += 1
        else:
            X[x] = 1
        if y in Y:
            Y[y] += 1
        else:
            Y[y] = 1
    for j, i in X.items():
        if i % 2 != 0:
            a = j
            break
    for j, i in Y.items():
        if i % 2 != 0:
            b = j
            break
    print(a, b)
