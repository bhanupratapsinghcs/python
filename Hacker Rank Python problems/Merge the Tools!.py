def merge_the_tools(string, k):
    n = len(string) // k
    str_lst = [x for x in string]
    str_for = []
    for i in range(0, len(str_lst), k):
        a = []
        for j in range(i, i + k):
            a.append(str_lst[j])
        str_for.append(a)
    for i in range(n):
        ans = []
        for j in str_for[i]:
            if ans.count(j) == 0:
                ans.append(j)
        print("".join(ans))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

 ########## input ############
# AABCAAADA
# 3
