def fact(a):
	if a == 0:
		return 1
	return a*fact(a-1)
n =3
print(fact(int(input())))