t = int(input())
for i in range(t):
    n = input()
    l = len(n)
    mn = 0
    ls = []
    if n[1:] == ("0" * (l - 1)):
        mn = 1
        ls.append(n)
        # print("yes", n)
    else:
        for x in range(l):
            r = n[l - x - 1]
            if r != "0":
                mn += 1
                ls.append(int(r) * pow(10, x))
    print(mn)
    for x in ls:
        print(x, end=" ")
    print()
