#------------------
# Author: Bhanu Pratap Singh
# Date  : Thu_14_Jan_2021
# Link  : https://codeforces.com/contest/1473/problem/D
#------------------
t = int(input())
for x in range(t):
	n, m = map(int, input().split())
	s = input()
	for i in range(m):
		l, r = map(int, input().split())
		r = 0
		mn, mx = 0, 0
		for x in range(1, n + 1):
			if x >= l and x <= r:
				print("---")
				pass
			else:
				if s[x - 1] == '+':
					r += 1
				else:
					r -= 1
			if mn > r:
				mn = r
			if mx < r:
				mx = r
		print(mx - mn)
