t = int(input())
for i in range(t):
    n = input()
    l = len(n)
    mn = 0
    ls = []
    if n[1:] == ("0" * (l - 1)):
        mn = 1
        ls.append(n)
        print("yes", n)
    else:
        for x in range(l - 1, 0):
            print(x, end=" ->")
