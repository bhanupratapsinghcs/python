t = int(input())
for x in range(t):
    a, b = map(int, input().split())
    if a % b == 0:
        print(0)
        continue
    print((((a // b) * b) + b) - a)
    # print(b-a%b)
