n = int(input())
x = 0
for i in range(n):
    s = input()
    if s == "X++":
        x += 1
    elif s == "X--":
        x - +1
    elif s == "++X" and i < n:
        x += 1
    elif s == "--X" and i < n:
        x -= 1
    elif s == "++X":
        x = x
    else:
        x = x

print(x)
