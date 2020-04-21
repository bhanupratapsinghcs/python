# n = "pratap"
# w = n.split()
# w.sort()
# for a in w:
# 	print(w)
# print(n)

# k, m =  map(int, input().split())
# for x in range(1,k+1):
# 	# lst[x],*line = input(int).split()
# 	# lste[x] = list(map(int,line))
# 	# c +=1
# 	exec("lst%s,*line = input(int).split()"%x)
# 	exec("lsye%s = list(map(int,line))"%x)
# print(k,m)
# print(lsye)


# from decimal import Decimal
# from itertools import groupby, islice
# from operator import itemgetter

# a = []
# for i in range(int(input())):
#   x, y = (input(), Decimal(input()))
#   a.append((y, x))
# a.sort()
# print(a)
# for k, v in islice(groupby(a, key=itemgetter(0)), 1, 2):
#   print()
#   for x in v:
#     print(x[1])


# # Program to sort alphabetically the words form a string provided by the user

# # change this value for a different result
# my_str = "Hello this Is an Example With cased letters"

# # uncomment to take input from the user
# #my_str = input("Enter a string: ")

# # breakdown the string into a list of words
# words = my_str.split()

# # sort the list
# words.sort()

# # display the sorted words

# print("The sorted words are:")
# for word in words:

# k, m =  map(int, input().split())
# for x in range(1,k+1):
# 	exec("lst%s,*line = input(int).split()"%x)
# 	exec("lsye%s = list(map(int,line))"%x)
# print(k,m)
# print(lsye)

# b = "bhanu"
# print(b[0:3])


# b = "how are you, how do you do?"
# c = b.find("how")
# print(c)
# b = b.lstrip("b")
# print(b)


# let us create a test string

# testString1 = "Hello World!"
# print("Original String: " + testString1)
# # Print this string in lower case

# # Converting a string to lower case
# print("Converting to LowerCase")
# print(testString1.lower())

# # Converting a string to upper case
# print("Converting to Upper Case")
# print(testString1.upper())

# # Capitalizing a string
# # Only the first letter in the string will be capitalized
# print("Capitalizing the String")
# print(testString1.capitalize())

# # Trying to slice out a substring between given indexes
# print("Substring from index 1 to 7")
# print(testString1[1:8])

# # Substring from the start till character at index = 7 (start of string is index 0)
# print("Substring from the start till character at index = 7 (start of string is index 0): ")
# print(testString1[:8])

# # Substring from the character at index = 7, till the end of the string (remember: start of string is index 0)
# print("Substring from the character at index = 7, till the end of the string (remember: start of string is index 0): ")
# print(testString1[7:])


# # Find the position of a  substring within the string
# # This gives us the first index during a left to right scan. If the string is not found, it returns -1
# print("Find the index from which the substring 'llo' begins within the test string")
# print(testString1.find('llo'))

# print("Now, let's look for a substring which is not a part of the given string")
# print(testString1.find('xxy'))

# # Now, trying to find the index of a substring between specified indexes only
# print("Now, trying to find a substring between specified indexes only: looking for 'l' between 4 and 9")
# print(testString1.find('l', 4, 9))

# # rfind is used, to find the index from the reverse
# # So, testString1.rfind('l') will look for the last index of l in the string
# print("find('l') on the given string returns the following index (scanning the string from left to right):")
# print(testString1.find('l'))

# print("rfind('l') on the given string returns the following index (this scans the string from right to left):")
# print(testString1.rfind('l'))

# # Now let us try to replace/substitute a substring of this string with another string
# print("Replacing World with Planet")
# print(testString1.replace("World", "Planet"))


# # Now let us try to split the string, into separate words
# # let us split it wherever there is a space
# print("Splitting the string into words, wherever there is a space")
# print(testString1.split(" "))
# print(testString1.rsplit(" "))
# # Remove leading and trailing whitespace characters
# # testString2 = "Hello World!  "
# # print("Current Test String=" + testString2)
# # print("Length (there are whitespaces at the end):" + len(testString2))
# # # print("Length after stripping " + len(testString2.strip()))

# import textwrap

# print(help(textwrap))

# # Replace all ______ with rjust, ljust or center.

# thickness = 5  # This must be an odd number
# c = 'H'

# # Top Cone
# for i in range(thickness):
#     print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

# # Top Pillars
# for i in range(thickness + 1):
#     print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# # Middle Belt
# for i in range((thickness + 1) // 2):
#     print((c * thickness * 5).center(thickness * 6))

# # Bottom Pillars
# for i in range(thickness + 1):
#     print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# # Bottom Cone
# for i in range(thickness):
#     print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))


# import textwrap

# value = """This function wraps the input paragraph such that each line
# in the paragraph is at most width characters long. The wrap method
# returns a list of output lines. The returned list
# is empty if the wrapped
# output has no content."""

# # Wrap this text.
# wrapper = textwrap.TextWrapper(width=50)

# word_list = wrapper.fill(text=value)

# # Print each line.
# # for element in word_list:
# print(word_list)

# tup = ({2})
# i = 1
# number = 63

# print(f"{i:b}".rjust(len(bin(number)) - len(bin(i)) - 2, ","))
#

# print(lambda x: x=print("name"))


# -----------------alphabet-rangoli--------------------
# size = 10
# s = "-"
# ascii_len = size + 96
# for i in range(1, size + 1):
#     print(s * ((size - i) * 2) + chr(ascii_len), end='')
#     for j in range(1, i):
#         print(s + chr(ascii_len - j), end="")
#     for k in range(i, 1, -1):
#         print(s + (chr(ascii_len + 2 - k)), end="")
#     print(s * ((size - i) * 2))

# # -------------lower half-------------
# for i in range(1, size):
#     print(s * ((i) * 2) + chr(ascii_len), end='')
#     for j in range(ascii_len - 1, 96 + i, -1):
#         print(s + chr(j), end="")
#     for k in range(98 + i, ascii_len + 1):
#         print(s + (chr(k)), end="")
#     print(s * ((i) * 2))


# ------------------------capitalize----------------------wrong answer
# def solve(s):
#     string = s.split(" ")
#     string1 = []
#     for i in string:
#         i = i.capitalize()
#         string1.append(i)
#     s = " ".join(string1)
#     return s

# if __name__ == '__main__':
#     # fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = "1 2 2 3 4 5 6 7 8  9"
#     solve(s)
#     # print(s)

#     # result = solve(s)

#     # fptr.write(result + '\n')

#     # fptr.close()
# nam = "ravi ravi"

# print(nam.count("ravi"))

# a = set(input().split())
# print(all(a > set(input().split()) for _ in range(int(input()))))


# from itertools import groupby

# print(list(groupby("1222311", key=int)))
# import tkinter


# class Application(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.create_widgets()

#     def create_widgets(self):
#         self.hi_there = tk.Button(self)
#         self.hi_there["text"] = "Hello World\n(click me)"
#         self.hi_there["command"] = self.say_hi
#         self.hi_there.pack(side="top")

#         self.quit = tk.Button(self, text="QUIT", fg="red",
#                               command=self.master.destroy)
#         self.quit.pack(side="bottom")

#     def say_hi(self):
#         print("hi there, everyone!")


# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()
# import os
print( &3 1)
