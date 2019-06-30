def print_formatted(number):
    for i in range(1, number + 1):
        g = len(bin(number)) - 2
        print(f"{i:d}".rjust(g, " ") + f"{i:o}".rjust(g + 1, " ") + f"{i:X}".rjust(g + 1, " ") + f"{i:b}".rjust(g + 1, " "))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
