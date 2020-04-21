t = int(input())
total_p = 0
for x in range(t):
    p = 0
    ls = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    temp = [0, 0, 0, 0]
    n = int(input())
    for i in range(n):
        m, tm = map(str, input().split())
        if m == 'A':
            temp[0] += 1
            if tm == "12":
                ls[0][0] += 1
            elif tm == '3':
                ls[0][1] += 1
            elif tm == '6':
                ls[0][2] += 1
            elif tm == '9':
                ls[0][3] += 1
        elif m == 'B':
            temp[1] += 1
            if tm == "12":
                ls[1][0] += 1
            elif tm == '3':
                ls[1][1] += 1
            elif tm == '6':
                ls[1][2] += 1
            elif tm == '9':
                ls[1][3] += 1
        elif m == 'C':
            temp[2] += 1
            if tm == "12":
                ls[2][0] += 1
            elif tm == '3':
                ls[2][1] += 1
            elif tm == '6':
                ls[2][2] += 1
            elif tm == '9':
                ls[2][3] += 1
        elif m == 'D':
            temp[3] += 1
            if tm == "12":
                ls[3][0] += 1
            elif tm == '3':
                ls[3][1] += 1
            elif tm == '6':
                ls[3][2] += 1
            elif tm == '9':
                ls[3][3] += 1
    m = []
    for j in range(4):
        m.append(max(ls[j]))
    m.sort(reverse=True)
    cnt = temp.count(0)
    p = (100 * m[0]) + (75 * m[1]) + (50 * m[2]) + (25 * m[3]) - (cnt * 100)
    total_p += p
    print(p)
print(total_p)


# partially solved
