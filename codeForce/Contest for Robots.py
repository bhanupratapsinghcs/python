n = int(input())
r = list(map(int, input().split()))
b = list(map(int, input().split()))
x = 0
y = 0
for i in range(n):
    if r[i] > b[i]:
        x += 1
    elif r[i] < b[i]:
        y += 1
if x != 0:
    print(y // x + 1)
else:
    print(-1)
