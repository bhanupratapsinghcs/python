n = 10

for i in range(1,n+1):
    b = 0
    print(" "*(n-i),end="")
    for j in range(0,i):
        # print(i)
        if j==b:
            print("0",end="")
            b=b+2
        else:
            print("1",end="")
        
        # print(b,end=" ")
    print("")