# # from collections import counter
# x = int(input())
# shoes_avl = list(map(int, input().split()))
# customer_no = int(input())
# # shoes_piece = counter(shoes_avl).values()
# earning = 0
# for x in range(customer_no):
#     size, price = map(int, input().split())
#     if size in shoes_avl:
#         earning += price
#         shoes_avl.remove(size)
# print(earning)


import collections

numShoes = int(input())
shoes = collections.Counter(map(int, input().split()))
print(shoes)
numCust = int(input())

income = 0

for i in range(numCust):
    size, price = map(int, input().split())
    if shoes[size]:
        print(shoes[size])
        income += price
        shoes[size] -= 1
print(income)
