t = int(input())
for x in range(t):
	n,k = map(int,input().split())
	ls = list(map(int,input().split()))
	print((sum(ls))%k)

# solved