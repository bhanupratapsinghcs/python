if __name__ == '__main__':
    n = int(input())
    lst = []
    for i in range(n):
        fh = list(map(str, input().split()))
        if fh[0] == "insert":
            lst.insert(int(fh[1]), int(fh[2]))
        elif fh[0] == "print":
            print(lst)
        elif fh[0] == "remove":
            lst.remove(int(fh[1]))
        elif fh[0] == "append":
            lst.append(int(fh[1]))
        elif fh[0] == "sort":
            lst.sort()
        elif fh[0] == "pop":
            lst.pop()
        else:
            lst.reverse()

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# [1, 48, 75, 30, 44, 6, 10, 44, 8, 9, 87, 75, 21, 2, 67, 12, 7, 66, 3, 5]
# [5, 3, 66, 7, 12, 67, 2, 21, 75, 87, 9, 8, 44, 10, 6, 44, 30, 75, 48, 1]
# [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 21, 30, 44, 44, 48, 66, 67, 75, 75, 87]
# [1, 3, 5, 6, 7, 8, 9, 10, 12, 21, 30, 44, 44, 48, 66, 67, 75, 75, 87, 2, 5]


# [1, 48, 75, 30, 44, 6, 10, 44, 8, 9, 87, 75, 21, 2, 67, 12, 7, 66, 3, 5]
# [87, 75, 75, 67, 66, 48, 44, 44, 30, 21, 12, 10, 9, 8, 7, 6, 5, 3, 2, 1]
# [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 21, 30, 44, 44, 48, 66, 67, 75, 75, 87]
# [1, 3, 5, 6, 7, 8, 9, 10, 12, 21, 30, 44, 44, 48, 66, 67, 75, 75, 87, 2, 5]
