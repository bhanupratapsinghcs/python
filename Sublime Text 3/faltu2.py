# def Towerofhanoi(n,sorc,ectr,dest):
# 	if n==1:
# 		print("move 1 from",sorc,"to",dest)
# 		return
# 	Towerofhanoi(n-1,sorc,dest,ectr)
# 	print("move ",n," from",sorc,"to",dest)
# 	Towerofhanoi(n-1,ectr,sorc,dest)
# n=int(input())
# Towerofhanoi(n,"sorc","ectr","dest")
# x=list(map(int,input().split()))
# sum=0
# for i in range(0,len(x)):
# 	sum=sum+x[i]
# avg=sum/len(x)
# print(avg)
# def saj(n,k):
# 	max=int(n[0])**2%k
# 	for i in range(len(n)):
# 		if max<(int(n[i])**2%k):
# 			max=int(n[i])**2%k
# 	return max
# n,k=input().split()
# n=int(n)
# k=int(k)
# sum=0
# for i in range(1,n+1):
# 	j=input().split()
# 	sum=sum+saj(j,k)
# print(sum)
fh = list(map(str, input().split()))
print(fh)
