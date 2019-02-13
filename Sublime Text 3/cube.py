
x = int(input())
y = int(input())
z = int(input())
n = int(input())
point= []
m = 0
for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k != n :
                    point.append([])
                    point[m]=[i,j,k]
                    m+=1
print(point)