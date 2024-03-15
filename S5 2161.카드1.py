import sys
from collections import deque
N= int(sys.stdin.readline().rstrip())
cards = deque(range(1,N+1))
if N==1:
    print(1)
else:
    while True:
        print(cards.popleft(),end=' ')
        cards.append(cards.popleft())
        if len(cards)==1:
            print(*cards)
            break
