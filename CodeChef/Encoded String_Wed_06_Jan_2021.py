#------------------
# Author: Bhanu Pratap Singh
# Date  : Wed_06_Jan_2021
#------------------

def encode_string(arr, n):
    t = [8, 4, 2, 1]
    r = ''
    c = 0
    for i in range(n):
        rm = i % 4
        if arr[i] == 0:
            c += 0
        else:
            c += t[rm]
        if (i + 1) % 4 == 0 and i != 0:
            r += chr(97 + c)
            c = 0
    return r


t = int(input())
for x in range(t):
    n = int(input())
    arr = list(map(int, input()))
    print(encode_string(arr, n))
