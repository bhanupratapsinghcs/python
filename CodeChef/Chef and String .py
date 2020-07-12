t = int(input())
for x in range(t):
    s = input()
    i = 0
    x = 0
    while(True):
        if i > (len(s) - 2):
            break
        if s[i + 1] != s[i]:
            x += 1
            i += 1
        i += 1
    print(x)
