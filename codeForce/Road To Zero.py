t = int(input())
for x in range(t):
    x, y = map(int, input().split())
    a, b = map(int, input().split())
    b = min(a + a, b)
    if x < y:
        x, y = y, x
    print(y * b + (x - y) * a)
