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


print(help(str))


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
# # print("Length after stripping " + len(testString2.strip()))
