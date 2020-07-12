t = int(input())
for x in range(t):
    ts = int(input())
    if ts > 2:
        if ts % 2 == 0:
            while ts % 2 == 0:
                ts //= 2
                if ts == 2:
                    break
            if ts == 2:
                print(0)
            else:
                print(ts // 2)
        else:
            print(ts // 2)
    else:
        print(0)
