import sys
from collections import deque
N=int(sys.stdin.readline().rstrip())
ans=deque()
for i in range(N):
    order = sys.stdin.readline().split()
    if order[0]=='1':
        ans.appendleft(order[1])
    elif order[0]=='2':
        ans.append(order[1])
    elif order[0]=='3':
        if ans:
            print(ans.popleft())
        else:
            print('-1')
    elif order[0]=='4':
        if ans:
            print(ans.pop())
        else:
            print('-1')
    elif order[0]=='5':
        print(len(ans))
    elif order[0]=='6':
        if ans:
            print('0')
        else:
            print('1')
    elif order[0]=='7':
        if ans:
            print(ans[0])
        else:
            print('-1')
    elif order[0]=='8':
        if ans:
            print(ans[-1])
        else:
            print('-1')
