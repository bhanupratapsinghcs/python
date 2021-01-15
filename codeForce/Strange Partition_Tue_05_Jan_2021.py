#------------------
# Author: Bhanu Pratap Singh
# Date  : Tue_05_Jan_2021
#------------------
from math import ceil


def starnge_partition(arr, n, x):
    r = 0
    for i in arr:
        r = r + ceil(i / x)
    return(ceil(sum(arr) / x), r)

# def beauty(arr):
#     a = []
#     for i in arr:
#         a.append(math.ceil(i / x))
#     return a


# def Strange_fun(arr, n, x):
#     a = []
#     a.append(sum(beauty(arr)))
#     i = 0
#     while(i < n - 1):
#         if math.ceil((arr[i] + arr[i + 1]) / x) < (math.ceil(arr[i] / x) + math.ceil(arr[i + 1] / 2)):
#             arr[i] = arr[i] + arr[i + 1]
#             arr.pop(i + 1)
#             if i != 0:
#                 i -= 1
#             n -= 1
#         else:
#             i += 1
#     a.append(sum(beauty(arr)))
#     return(min(a), max(a))


t = int(input())
for x in range(t):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    mn, mx = starnge_partition(arr, n, x)
    print(mn, mx)
