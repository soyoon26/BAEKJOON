N = int(input())
students = [list(input().split()) for _ in range(N)]
students.sort(key=lambda students:(-int(students[1]),int(students[2]),-int(students[3]),students[0]))
for i in range(N):
    print(students[i][0])