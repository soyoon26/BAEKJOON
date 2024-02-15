from collections import deque
import sys

N,M=map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited=[]
for i in range(M):
    u, v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
def bfs(r):
    queue = deque([r])
    visited.append(r)
    while queue:
        V=queue.popleft()
        for j in graph[V]:
            if j not in visited:
                visited.append(j)
                queue.append(j)
cnt=0
for k in range(1,N+1):
    if k not in visited:
        cnt+=1
        bfs(k)
print(cnt)

#for문 돌리지 않고 visited를 False로 셋팅한 뒤 False인 곳을 시작점이 되게 while 돌림