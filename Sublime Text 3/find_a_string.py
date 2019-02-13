def count_substring(string, sub_string):
	i = 0
	for i in range(len(string)):
		for j in range(len(sub_string)):
			if string[j] == sub_string[j]:
				i = i+1
	return i//len(sub_string)

if __name__ == '__main__':
	string =" ABCDCDC"
	sub_string = "CDC"

	count = count_substring(string, sub_string)
	print(count)
