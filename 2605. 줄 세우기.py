N = int(input()) #학생수
num_lst = list(map(int,input().split())) #[0, 1, 1, 3, 2]
stu_lst = [i for i in range(1,N+1)] #[1, 2, 3, 4, 5]
queue = []

for i in range(N):
    M = len(queue)
    queue.insert(M-num_lst[i],stu_lst[i])
print(*queue)