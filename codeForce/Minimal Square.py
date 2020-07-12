t = int(input())
for x in range(t):
    a, b = map(int, input().split())
    if a < b:
        a, b = b, a
    if a > (b + b):
        print(pow(a, 2))
    else:
        print(pow((b + b), 2))
