def leapyear(x):
	for i in range(4,x+4,4):
		if (i%100 == 0):
			print()
		else:
			print(i,end=" ")
y = int(input())
for i in range(1,y+1):
    if (i%400 == 0):
        print(i,end=" ")
    elif (i%4==0 and i%100 != 0) :
        print(i,end=" ")
print("")            
leapyear(int(input()))        