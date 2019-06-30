n = 'qA2'
a = [False for j in range(5)]
n = set(n)
for i in n:
    if i.isdigit():
        a[2] = True
        a[0] = True
    elif i.islower():
        a[3] = True
        a[1] = True
        a[0] = True
    elif i.isupper():
        a[4] = True
        a[0] = True
        a[0] = True
for k in a:
    print(k)
