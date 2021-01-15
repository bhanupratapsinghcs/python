#------------------
# Author: Bhanu Pratap Singh
# Date  : Wed_06_Jan_2021
# Link  : https://www.codechef.com/JAN21C/problems/FAIRELCT
#------------------
def fair_election(a, b, n, m):
    john = sum(a)
    jack = sum(b)
    if john > jack:
        return 0
    a.sort()
    b.sort(reverse=True)
    r = 0
    for i in range(min(n, m)):
        john = john - a[i] + b[i]
        jack = jack - b[i] + a[i]
        r += 1
        if john > jack:
            return r
    if jack >= john:
        return -1
    else:
        return 0


t = int(input())
for x in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(fair_election(a, b, n, m))
