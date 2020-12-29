t = int(input())
for x in range(t):
    h, p = map(int, input().split())
    if p > h // 2:
        print(1)
    else:
        print(0)
