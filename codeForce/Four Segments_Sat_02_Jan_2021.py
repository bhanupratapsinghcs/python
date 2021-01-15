#------------------
# Author: Bhanu Pratap Singh
# Date  : Sat_02_Jan_2021
#------------------

def find_max_area(arr):
    arr.sort()
    return (arr[0] * arr[2])


t = int(input())
for x in range(t):
    arr = list(map(int, input().split()))
    print(find_max_area(arr))
