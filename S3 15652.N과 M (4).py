N,M = map(int,input().split())
answer_candi=[]
answer=[]
def back(start):
    if len(answer) == M:
        print(*answer)
        return
    for i in range(start,N+1):
        answer.append(i)
        back(i)
        answer.pop()
back(1)

