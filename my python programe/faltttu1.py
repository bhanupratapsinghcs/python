# n = "pratap"
# w = n.split()
# w.sort()
# for a in w:
#   print(w)
# print(n)

# k, m =  map(int, input().split())
# for x in range(1,k+1):
#   # lst[x],*line = input(int).split()
#   # lste[x] = list(map(int,line))
#   # c +=1
#   exec("lst%s,*line = input(int).split()"%x)
#   exec("lsye%s = list(map(int,line))"%x)
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
#   exec("lst%s,*line = input(int).split()"%x)
#   exec("lsye%s = list(map(int,line))"%x)
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
# print( &3 1)
# m, n = int(input())
# j = "7"
# print(chr(97))
# print("0" * 0)
# ls = {}
# ls[1] = 1
# print(ls)
# # print([1 += 19])

# print(sorted([16, 19, 11, 15, 10, 12, 14]))
# print(7 // 3)
# s = 'lexicographically'
# S = list(s)
# S.sort()
# s = ''.join(S)
# print(help(str))


# bubble
# a = [16, 19, 11, 15, 10, 12, 14]
#   for j in range(len(a)):
#       swapped = False
#       i = 0
#       while i < len(a) - 1:
#           if a[i] > a[i + 1]:
#               a[i], a[i + 1] = a[i + 1], a[i]
#               swapped = True
#               i = i + 1
#           if swapped == False:
#               break
# print(a)

# Insertion
# def insertionSort(nlist):
#     for index in range(1, len(nlist)):
#         currentvalue = nlist[index]
#         position = index
#         while position > 0 and nlist[position - 1] > currentvalue:
#             nlist[position] = nlist[position - 1]
#             position = position - 1
#             nlist[position] = currentvalue


# nlist = [14, 46, 43, 27, 57, 41, 45, 21, 70]
# insertionSort(nlist)
# print(nlist)


# selection

# A = [64, 25, 12, 22, 11]
# for i in range(len(A)):
#  min_idx = i
#  for j in range(i+1, len(A)):
#  if A[min_idx] > A[j]:
#  min_idx = j

#  A[i], A[min_idx] = A[min_idx], A[i]
# print ("Sorted array")
# for i in range(len(A)):
#  print("%d" %A[i])

# Merge

# def mergeSort(myList):
#     if len(myList) > 1:
#         mid = len(myList) // 2
#         left = myList[:mid]
#         right = myList[mid:]
#         mergeSort(left)
#         mergeSort(right)
#         i = 0
#         j = 0
#         k = 0

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             myList[k] = left[i]
#             i += 1
#         else:
#             myList[k] = right[j]
#             j += 1

#         k += 1

#     while i < len(left):
#         myList[k] = left[i]
#         i += 1
#         k += 1
#     while j < len(right):
#         myList[k] = right[j]
#         j += 1
#         k += 1


# myList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# mergeSort(myList)
# print(myList)

# quick

# def partition(arr, low, high):
#     i = (low - 1)
#     pivot = arr[high]
#     for j in range(low, high):
#         if arr[j] < pivot:
#             i = i + 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return (i + 1)


# def quickSort(arr, low, high):
#     if low < high:
#         pi = partition(arr, low, high)
#         quickSort(arr, low, pi - 1)
#         quickSort(arr, pi + 1, high)


# arr = [10, 7, 8, 9, 1, 5]
# n = len(arr)
# quickSort(arr, 0, n - 1)
# print("Sorted array is:")
# for i in range(n):
#     print("%d" % arr[i])

# def heapify(arr, n, i):
#     largest = i  # Initialize largest as root
#     l = 2 * i + 1     # left = 2*i + 1
#     r = 2 * i + 2     # right = 2*i + 2

#     # See if left child of root exists and is
#     # greater than root
#     if l < n and arr[i] < arr[l]:
#         largest = l

#     # See if right child of root exists and is
#     # greater than root
#     if r < n and arr[largest] < arr[r]:
#         largest = r

#     # Change root, if needed
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]  # swap

#         # Heapify the root.
#         heapify(arr, n, largest)

# # The main function to sort an array of given size


# def heapSort(arr):
#     n = len(arr)

#     # Build a maxheap.
#     for i in range(n // 2 - 1, -1, -1):
#         heapify(arr, n, i)

#     # One by one extract elements
#     for i in range(n - 1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]  # swap
#         heapify(arr, i, 0)


# # Driver code to test above
# arr = [12, 11, 13, 5, 6, 7]
# heapSort(arr)
# n = len(arr)
# print("Sorted array is")
# for i in range(n):
#     print("%d" % arr[i])
# def heapify(arr, n, i):
#     largest = i  # Initialize largest as root
#     l = 2 * i + 1     # left = 2*i + 1
#     r = 2 * i + 2     # right = 2*i + 2

#     if l < n and arr[i] < arr[l]:
#         largest = l

#     if r < n and arr[largest] < arr[r]:
#         largest = r

#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]  # swap

#         heapify(arr, n, largest)


# def heapSort(arr):
#     n = len(arr)

#     for i in range(n // 2 - 1, -1, -1):
#         heapify(arr, n, i)

#     for i in range(n - 1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]  # swap
#         heapify(arr, i, 0)


# arr = [12, 11, 13, 5, 6, 7]
# heapSort(arr)
# n = len(arr)
# print("Sorted array is")
# for i in range(n):
#     print("%d" % arr[i])


# counting sort

# Counting sort in Python programming


# def countingSort(array):
#     size = len(array)
#     output = [0] * size

#     # Initialize count array
#     count = [0] * 10

#     # Store the count of each elements in count array
#     for i in range(0, size):
#         count[array[i]] += 1

#     # Store the cummulative count
#     for i in range(1, 10):
#         count[i] += count[i - 1]

#     # Find the index of each element of the original array in count array
#     # place the elements in output array
#     i = size - 1
#     while i >= 0:
#         output[count[array[i]] - 1] = array[i]
#         count[array[i]] -= 1
#         i -= 1

#     # Copy the sorted elements into original array
#     for i in range(0, size):
#         array[i] = output[i]


# data = [4, 2, 2, 8, 3, 3, 1]
# countingSort(data)
# print("Sorted Array in Ascending Order: ")
# print(data)


# import requests


# def send_simple_message():
#     return requests.post(
#         "https://api.mailgun.net/v3/sandbox5574f0787be94b13888f4ff628bdb550.mailgun.org/messages",
#         auth=("api", "812ac9d374feb9cc87cbb78029b7e4d7-c50a0e68-d1b805d3"),
#         data={"from": "Excited User <bhanu.singh_cs18@gla.ac.in>",
#               "to": "pbhanu0501@gmail.com",
#               "subject": "Hello",
#               "text": "Testing some Mailgun awesomness!"})


# print(send_simple_message())
