import sys
from collections import deque
N=int(sys.stdin.readline().rstrip())
num=deque(range(1,N+1))
while len(num) != 1:
    num.popleft()
    num.append(num.popleft())
print(*num)