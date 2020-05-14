n, k = map(int, input().split())
ls = list(map(int, input().split()))
a = ls[k + 1]
print(ls)
rs = 0
print(ls[k + 1])
for i in range(n):
    if ls[i] >= ls[k + 1]:
        rs += 1
        print(i)
print(rs - 1)
