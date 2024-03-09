from collections import deque
N,K=map(int,input().split())
people=deque(range(1,N+1))
answer=[]
while people:
    people.rotate(-K+1)
    answer.append(people.popleft())
print('<',end='')
print(*answer,sep=', ',end='>')



