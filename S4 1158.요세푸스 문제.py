import sys
from collections import deque
N,K=map(int,sys.stdin.readline().split())
num=deque()
for i in range(1,N+1):
      num.append(i)
print('<',end='')
if K>1:
    while len(num) != 1:
        for k in range(K-1):
            num.append(num.popleft())
        print(num.popleft(),end=', ')
print(*num,sep=', ',end='')
print('>')
