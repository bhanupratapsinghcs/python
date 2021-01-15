#------------------
# Author: Bhanu Pratap Singh
# Date  : Mon_04_Jan_2021
# Link  : https://codeforces.com/contest/1472/problem/B
#------------------

def fair_division(arr, n):
    o = arr.count(1)
    t = arr.count(2)
    if o % 2 != 0:
        return "NO"
    if t % 2 != 0 and o == 0:
        return "NO"
    else:
        return "YES"


t = int(input())
for x in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(fair_division(arr, n))
