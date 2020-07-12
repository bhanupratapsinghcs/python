t = int(input())
for i in range(t):
    n = int(input())
    hn = n // 2
    sm1 = pow(2, n)
    sm2 = 0
    for j in range(1, hn):
        sm1 += pow(2, j)
    for j in range(hn, n):
        sm2 += pow(2, j)
    print(sm1 - sm2)
