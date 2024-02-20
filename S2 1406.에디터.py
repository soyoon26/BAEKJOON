import sys
from collections import deque
line = deque(sys.stdin.readline().rstrip())
stack1=line
stack2=deque()
M=int(sys.stdin.readline().rstrip())
for i in range(M):
    order=sys.stdin.readline().split()
    if order[0]=='L' and stack1:
        stack2.appendleft(stack1.pop())
    elif order[0]=='D' and stack2:
        stack1.append(stack2.popleft())
    elif order[0]=='B' and stack1:
        stack1.pop()
    elif order[0]=='P':
        stack1.append(order[1])
print(*stack1,*stack2,sep='')


#remove값은 인덱스값이 아니라 앞에서 비교해서 같으면 지움