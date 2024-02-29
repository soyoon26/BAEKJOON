from collections import deque
N,K=map(int,input().split())
squirrel=deque(range(1,N+1))

while len(squirrel) != 1:
    squirrel.rotate(-1)
    for i in range(K-1):
        squirrel.popleft()
        if len(squirrel) == 1:
            break
print(*squirrel)
