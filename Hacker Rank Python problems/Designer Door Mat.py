n, m = input().split()
a = int(n) // 2
b = int(m) // 2
c = '.|.'
for i in range(a):
    print((c * i).rjust(b - 1, '-') + c + (c * i).ljust(b - 1, '-'))
print("WELCOME".center(int(m), '-'))
for i in range(a):
    print((c * (a - i - 1)).rjust(b - 1, '-') + c + (c * (a - i - 1)).ljust(b - 1, '-'))

# Sample Input:-
# 5 15
# 7 21
# 4 12 not an input