#------------------
# Author: Bhanu Pratap Singh
# Date  : Thu_14_Jan_2021
# Link  : https://www.codechef.com/JAN21C/problems/BILLRD
#------------------
def points(k, ox, oy, x, y):
    if k % 4 == 1:
        return (x, y)
    elif k % 4 == 2:
        return (y, x)
    elif k % 4 == 3:
        return (oy, ox)
    else:
        return (ox, oy)


def find_impact(n, k, ox, oy):
    if ox == oy:
        return (n, n)
    if ox > oy:
        x = n
        y = oy + n - ox
        ox = ox - oy
        oy = 0
        return points(k, ox, oy, x, y)
    else:
        y = n
        x = ox + n - oy
        oy = oy - ox
        ox = 0
        return points(k, ox, oy, x, y)


t = int(input())
for x in range(t):
    n, k, x, y = map(int, input().split())
    rx, ry = find_impact(n, k, x, y)
    print(rx, ry)
