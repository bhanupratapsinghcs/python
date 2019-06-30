n, m = (input().split())
n, m = int(n), int(m)
lst = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))
h = 0
s = 0
for i in lst:
    if (i in a and i in b):
        pass
    elif i in a:
        h += 1
    elif i in b:
        s += 1

print(h - s)
