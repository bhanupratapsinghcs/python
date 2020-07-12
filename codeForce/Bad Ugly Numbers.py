t = int(input())
for x in range(t):
    n = int(input())
    if n == 1:
        print(-1)
    else:
        print("2" + "3" * (n - 1))
