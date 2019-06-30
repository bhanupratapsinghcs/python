size = 26
s = "-"
ascii_len = size + 96
for i in range(1, size + 1):
    print(s * ((size - i) * 2) + chr(ascii_len), end='')
    for j in range(1, i):
        print(s + chr(ascii_len - j), end="")
    for k in range(i, 1, -1):
        print(s + (chr(ascii_len + 2 - k)), end="")
    print(s * ((size - i) * 2))

# -------------lower half-------------
for i in range(1, size):
    print(s * ((i) * 2) + chr(ascii_len), end='')
    for j in range(ascii_len - 1, 96 + i, -1):
        print(s + chr(j), end="")
    for k in range(98 + i, ascii_len + 1):
        print(s + (chr(k)), end="")
    print(s * ((i) * 2))
