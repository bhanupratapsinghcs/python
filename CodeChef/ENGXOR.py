from sys import stdin, stdout
t = int(stdin.readline())
for i in range(t):
    n, q = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    for j in range(q):
        p = int(stdin.readline())
        cnt = 0
        for e in a:
            temp = (e ^ p)

            cnt += (prty & 1)
        stdout.write(str(n - cnt) + " " + str(cnt) + "\n")
# 2
# 6 1
# 4 2 15 9 8 8
# 3
# 6 2
# 1 2 4 6 8 0
# 3
# 4
