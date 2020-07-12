t = int(input())
for x in range(t):
    k = int(input())
    t = 0
    for i in range(1, 9):
        for j in range(1, 9):
            t += 1
            if j == 1 and i == 1:
                print('O', end="")
            elif t > k:
                print('X', end="")
            else:
                print('.', end="")
        print()
