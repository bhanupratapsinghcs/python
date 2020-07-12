t = int(input())
for x in range(t):
    n = int(input())
    ls = list(map(int, input().split()))
    print(len(set(ls)))
