from itertools import product
a = list(map(int, input().split()))
b = list(map(int, input().split()))
[print(x,end=" ") for x in list(product(a, b))]


#  print list(product([1,2,3],[3,4]))
# [(1, 3), (1, 4), (2, 3), (2, 4), (3, 3), (3, 4)]