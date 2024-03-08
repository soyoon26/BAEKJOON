from collections import deque
import sys
Deque=deque()
N=int(sys.stdin.readline().rstrip())
for n in range(N):
    order=sys.stdin.readline().split()
    if order[0]=='push_front':
        Deque.appendleft(order[1])
    elif order[0]=='push_back':
        Deque.append(order[1])
    elif order[0]=='pop_front':
        if Deque:
            print(Deque.popleft())
        else:
            print(-1)
    elif order[0]=='pop_back':
        if Deque:
            print(Deque.pop())
        else:
            print(-1)
    elif order[0]=='size':
        print(len(Deque))
    elif order[0]=='empty':
        if Deque:
            print(0)
        else:
            print(1)
    elif order[0]=='front':
        if Deque:
            print(Deque[0])
        else:
            print(-1)
    elif order[0]=='back':
        if Deque:
            print(Deque[-1])
        else:
            print(-1)