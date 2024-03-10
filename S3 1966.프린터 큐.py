import sys
from collections import deque
T=int(sys.stdin.readline().rstrip())
for t in range(T):
    N,M=map(int,sys.stdin.readline().split())
    n=list(map(int,sys.stdin.readline().split()))
    n_deque=deque()
    for i in range(N):
        n_deque.append([i,n[i]])
    cnt=0
    while True:
        if max(n_deque, key=lambda x : x[1]) != n_deque[0]:
            n_deque.append(n_deque.popleft())
        else:
            cnt+=1
            if n_deque[0] == [M,n[M]]:
                break
            n_deque.popleft()
    print(cnt)

#ar1 = deque((p, idx) for idx, p in enumerate(arr))