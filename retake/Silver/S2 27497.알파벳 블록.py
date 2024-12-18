import sys
from collections import deque
stack=deque()
orders=[]
N=int(sys.stdin.readline().rstrip())
for i in range(N):
    order=sys.stdin.readline().split()
    if order[0]=='1':
        orders.append(order[0])
        stack.append(order[1])
    elif order[0]=='2':
        orders.append(order[0])
        stack.appendleft(order[1])
    elif order[0]=='3' and stack:
        if orders.pop()=='1':
            stack.pop()
        else:
            stack.popleft()

if len(stack)==0:
    print(0)
else:
    print(*stack,sep='')
