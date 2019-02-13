if __name__ == '__main__':
	students = []
	for _ in range(int(input())):
		name = input()
		score = float(input())
		students.append([name,score])

students = sorted(students,key = lambda x:x[1])

# scnd_hgh = [students[i+1][1] for i in range(len(students)) if students[i+1][1]>students[i][1]]
# scnd_hgh = int(scnd_hgh)

for i in range(len(students)):
	if students[i+1][1]>students[i][1]:
		scnd_hgh = students[i+1][1]
		break

sclt = []
for i in range(len(students)):
	if students[i][1]==scnd_hgh:
		sclt.append([students[i][0],students[i][1]])

sclt = sorted(sclt,key = lambda x:x[0])

for i in range(len(sclt)):
	print(sclt[i][0])

# input :-|

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39