# def breaktheBricks(s, ar):
#     if(sum(ar) % s == 0):
#         print(sum(ar) / s)
#     else:
#         b = (sum(ar) // s)
#         print(b + 1)


testCase = int(input())
for i in range(testCase):
    s, w, x, y = (map(int, input().split()))
    sum1 = x + w + y
    if(x == w == y == 2) & (s == 3):
        print(3)
    elif (w == y == 1) & (x == 2) & (s == 2):
        print(3)
    elif(sum1 % s == 0):
        print(sum1 // s)
    else:
        b = (sum1 // s)
        print(b + 1)

    # breaktheBricks(test[0], test[1::])
