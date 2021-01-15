#------------------
# Author: Bhanu Pratap Singh
# Date  : Thu_14_Jan_2021
# Link  : https://codeforces.com/contest/1473/problem/A
#------------------
def function(arr, n, d):
    r = 0
    for i in arr:
        if i > d:
            r += 1
            break
    if r == 0:
        return "YES"
    else:
        arr.sort()
        if arr[0] + arr[1] <= d:
            return "YES"
    return "NO"


t = int(input())
for x in range(t):
    n, d = map(int, input().split())
    arr = list(map(int, input().split()))
    print(function(arr, n, d))
