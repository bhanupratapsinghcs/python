def minion_game(string):
    vwl = ['A', 'E', 'I', 'O', 'U']
    stuart = 0
    kevin = 0
    # correct Answer----------
    # vwl = ['A', 'E', 'I', 'O', 'U']
    # stuart = 0
    # kevin = 0
    # n = len(string)
    # for i in range(len(string)):
    #     if string[i] in ('A', 'E', 'I', 'O', 'U'):
    #         kevin = kevin + n - i
    #     else:
    #         stuart += n - i
    # ---------------------------
    for i in range(len(string)):
        ctr = 0
        for wrd in range(len(string) - i, 0, -1):
            # print(string[ctr:ctr + i + 1])
            if string[ctr:ctr + i + 1][0] in vwl:
                kevin += 1
            else:
                stuart += 1
            ctr += 1
    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
