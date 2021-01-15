#------------------
# Author: Bhanu Pratap Singh
# Date  : Wed_06_Jan_2021
#------------------
def division3(arr, k, d):
    s = sum(arr) // k
    if s > d:
        return d
    else:
        return s


t = int(input())
for x in range(t):
    n, k, d = map(int, input().split())
    arr = list(map(int, input().split()))
    print(division3(arr, k, d))
