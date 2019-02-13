def hcf(n,p):
	max1,e=0,0
	max1=n
	if p<n:
		max1=p
	for i in range(1,max1+1) :
		if n%i==0 and p%i==0:
			e=i
	print(e)
n, p = input().split() 
n=int(n)
p=int(p)
a='''
if p>n:
	for k in range(1,p) :
		if n%k==0 and p%k==0:
			h=k
else:
	for g in range(1,n) :
		if n%g==0 and p%g==0:
			h=g			
print(h)
'''
hcf(n,p)	