#------------------
# Author: Bhanu Pratap Singh
# Date  : Sat_02_Jan_2021
#------------------

def restore(s, n):
    r = []
    t = 0
    for x in range(n):
        if x % 2 == 0:
            r.append(s[t])
        else:
            r.append(s[n - 1 - t])
            t += 1
    print(" ".join(r))


t = int(input())
for x in range(t):
    n = int(input())
    arr = list(map(str, input().split()))
    restore(arr, n)
