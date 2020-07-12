t = int(input())
for x in range(t):
    n, m = map(int, input().split())
    print('W' + ('\n'.join(['B' * m] * n)[1:]))
