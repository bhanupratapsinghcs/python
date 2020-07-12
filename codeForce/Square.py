t = int(input())
for i in range(t):
	# print(i + 1, "------")
	a1, b1 = map(int, input().split())
	a2, b2 = map(int, input().split())
	# print(a1, b1, a2, b2)
	c  = 0
	if a1 == a2:
		if b1 + b2 == a1:
			c +=1
	if b1 == a2:
		if a1 + b2 == b1:
			c +=1
	if a1 == b2:
		if a2 + b1 == a1:
			c +=1
	if b1 == b2:
		if a1 + a2 == b1:
			c +=1
	if c>0:
		print("Yes")
	else:
		print("No")
