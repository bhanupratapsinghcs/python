n = input()
q = int(n)
if q%4==0 or q%7==0:
	print("YES")
elif "4" in n or "7" in n:
	if n.count('4')+n.count('7')==len(n):
		print("YES")
	else:
		print("NO")
else:
	print("NO")