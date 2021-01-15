#------------------
# Author: Bhanu Pratap Singh
# Date  : Mon_04_Jan_2021
#------------------

def function(w, h, n):
    if w % 2 != 0 and h % 2 != 0:
        if n > 1:
            # print('-1')
            return "NO"
        # print('-2-')
        return "YES"
    else:
        if w % 2 == 0 and h % 2 == 0:
            c = 1
            while(w % 2 == 0):
                c += c
                w //= 2
            c *= 2
            if n > c:
                # print('--7-'/)
                return "NO"
            # print('---8-')
            return "YES"
        if w % 2 == 0:
            c = 1
            while(w % 2 == 0):
                c += c
                w //= 2
            if n > c:
                # print('--3-')
                return "NO"
            # print('---4-')
            return "YES"
        else:
            c = 1
            while(h % 2 == 0):
                c += c
                h //= 2
            if n > c:
                # print('-----5')
                return "NO"
            # print('------6')
            return "YES"


t = int(input())
for x in range(t):
    w, h, n = map(int, input().split())
    print(function(w, h, n))
