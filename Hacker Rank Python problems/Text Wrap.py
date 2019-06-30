import textwrap

# def wrap(string, max_width):
#     result1 = textwrap.wrap(text=string, width=max_width)
#     result = ""
#     i = 0
#     for element in result1:
#         result = result + "\n"*i + element
#         i = 1
#     return result


def wrap(string, max_width):
    result1 = textwrap.TextWrapper(width=max_width)
    result = result1.fill(text=string)

    return result


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# sample input :-

# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
