n = int(input())
k = int(input())
print(" "*(n-1)+"*")
for i in range(n-1):
	if (i == (k-2)):
		print(" "*(n-i-2)+"**"+"*"*(2*i),end="*\n")
	else:
		print(" "*(n-i-2)+"* "+" "*(2*i),end="*\n")
		continue
arr = arry()

#        *
#      *   *
#     *     *
#    *********
#   *         *
#  *           *
# *             *