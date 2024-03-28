N,M=map(int,input().split())
answer=[]
def back():
    if len(answer) == M:
        print(*answer)
        return
    for i in range(1,N+1):
        answer.append(i)
        back()
        answer.pop()
back()