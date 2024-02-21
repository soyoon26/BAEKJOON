import sys
from collections import deque
T=int(sys.stdin.readline().rstrip())
for t in range(T):
    pw=sys.stdin.readline().rstrip()
    stack1=[]
    stack2=deque()
    for i in pw:
        if i == '<' and stack1:
            stack2.appendleft(stack1.pop())
        elif i == '>' and stack2:
            stack1.append(stack2.popleft())
        elif i == '-' and stack1:
            stack1.pop()
        elif i !='<' and i != '>' and i != '-':
            stack1.append(i)
    print(*stack1,*stack2,sep='')

#left안 쓰고 stack2를 역으로 출력해도 됨