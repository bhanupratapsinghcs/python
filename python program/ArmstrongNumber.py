n = input()
l = len(n)
n = int(n)
n1 = n
s = 0
while n!= 0:
	temp = n%10
	s = s+(temp**l)
	n//=10
if s==n1:
	print("Armstrong Number.")
else:
	print("Not Armstrong.")
