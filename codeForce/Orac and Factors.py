# def sd(a):
#     x = 2
#     while x <= a:
#         if a % x == 0:
#             return x
#             break
#         x += 1


# smallest divisor function above
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    if n % 2 == 0:
        print(n + 2 * k)
    else:
        d = 0
        for x in range(2, n + 1):
            if n % x == 0:
                d = x
                break
        print(n + 2 * (k - 1) + d)
