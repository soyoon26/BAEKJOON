#N = int(input())
#student=[input().split() for _ in range(N)]

#for i in range(len(student)-1,-1,-1):
#    for j in range(i):
#        if student[j][0]>student[j+1][0]:
#            temp = student[j]
#            student[j]=student[j+1]
#            student[j+1]=temp
#for i in student:
#    print(*i)
#시간초과


N = int(input())
student = [list(input().split()) for _ in range(N)]
student.sort(key = lambda x : int(x[0]))
for i in member:
    print(*i)