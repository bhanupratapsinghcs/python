def count_substring(string, sub_string):
    x = 0
    for i in range(len(string)):
        # print(string[i:len(sub_string) + i])
        if sub_string == string[i:len(sub_string) + i]:
            x = x + 1
    return x


if __name__ == '__main__':
    string = " ABCDCDC"
    sub_string = "CDC"

    count = count_substring(string, sub_string)
    print(count)
