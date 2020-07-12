t = int(input())
for x in range(t):
    n = int(input())
    ls = list(map(int, input().split()))
    cnt = 0
    if n == 1:
        print(cnt + 1)
    else:
        for i in range(n - 1):
            if i == 0:
                if ls[0] > max(ls[1:]):
                    print(1)
                    cnt += 1
                    break
                elif ls[0] > ls[1]:
                    print(2)
                    cnt += 1
                    continue
                elif ls[0] <= ls[1]:
                    print(3)
                    continue
            if max(ls[:i]) < ls[i] and ls[i + 1] < ls[i]:
                print(4)
                cnt += 1
            if max(ls[i + 1:n]) > ls[i]:
                print(5)
                break
    print(cnt)
