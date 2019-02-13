if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks
        student_marks[name] = scores
    query_name = input()
av = sum(student_marks[query_name]) / 3
print("%.2f" % float(av))

# Standard Output:-
# 
# 2
# Harsh 25 26.5 28
# Anurag 26 28 30
# Harsh
