y = int(input())
l = int(input())
r = pow(y, l)
m = r % 9
if m == 0:
    print(9)
else:
    print(m)
