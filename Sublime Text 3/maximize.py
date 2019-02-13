# # maxamize it
# 3 1000
# 2 5 4
# 3 7 8 9 
# 5 5 7 8 9 10

		# name, *line = input().split()
  		#scores = list(map(float, line))

# x, y = map(int, raw_input().split()) input in one line


k, m =  map(int, input().split())
mn = m/k
sm = []
tmp = []
for x in range(k):
	ln , *line = input(int).split()
	tmp = (map(int,line) for i in range(int(ln)))
	



# for x in range(1,k+1):
# 	exec("lst%s,*line = input(int).split()"%x)
# 	exec("lsye%s = list(map(int,line))"%x)
# for i in range(1,k+1):
# 	exec("lsye%s.sort(reverse = True)"%i)
# mn = m/k
# sm = []
# for i in range(2):
# 	if lsye1[i]<mn:
# 		sm.append(lsye1[i])
# 		break

# print(k,m)
# print(lsye1,sm)