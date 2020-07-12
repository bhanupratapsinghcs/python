t = int(input())
for x in range(t):
    n, k = map(int, input().split())
    n1 = list(map(int, input().split()))
    n2 = list(map(int, input().split()))
    n1 = sorted(n1)
    n2 = sorted(n2)
    for i in range(k):
        if n1[i] < n2[n - i - 1]:
            n1[i] = n2[n - 1 - i]
    # print(n1)
    print(sum(n1))
