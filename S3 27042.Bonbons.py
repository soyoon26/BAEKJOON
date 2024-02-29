from collections import deque
N=int(input())
cows=deque(range(0,N+1))
while len(cows) != 1:
    cows.popleft()
    cows.rotate(-1)
print(*cows)
