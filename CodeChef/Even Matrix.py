t = int(input())
for x in range(t):
    n = int(input())
    k = 1
    if n % 2 != 0:
        for i in range(n):
            for j in range(n):
                print(k, end=" ")
                k += 1
            print()
    else:
        for i in range(n):
            if i % 2 == 0:
                for j in range(n):
                    print(k, end=" ")
                    k += 1
            else:
                k += n - 1
                for j in range(n):
                    print(k, end=" ")
                    k -= 1
                k += n + 1
            print()
