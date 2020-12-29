t = int(input())
# print(help(str))
for x in range(t):
    s = input()
    p = input()
    s = ''.join(sorted(s))
    r = ""
    for i in set(s):
