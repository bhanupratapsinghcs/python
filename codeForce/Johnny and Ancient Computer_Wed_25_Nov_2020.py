import math
d1, v1, d2, v2, p = map(int, input().split())
if d1 > d2:
    m = d1 - d2
    if p < (v2 * m):
        d = math.ceil(p / v2) + d2 - 1
    else:
        p = p - (v2 * m)
        d = math.ceil(p / (v1 + v2)) + m + d2 - 1
elif d2 > d1:
    m = d2 - d1
    if p < (v1 * m):
        d = math.ceil(p / v1) + d1 - 1
    else:
        p = p - (v1 * m)
        d = math.ceil(p / (v1 + v2)) + m + d1 - 1
else:
    d = math.ceil(p / (v1 + v2)) + d1 - 1
print(d)
