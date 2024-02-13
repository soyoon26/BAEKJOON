import sys
from collections import deque
M, N = map(int,sys.stdin.readline().rstrip().split())
visited=[]
unvisited=[]
graph=[[] for _ in range(M+1)]
for i in range(N):
    u ,v = map(int,sys.stdin.readline().rstrip().split())
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

bfs(1)
for k in range(1,M+1):
    if k not in visited:
        unvisited.append(k)

if len(unvisited) == 0:
    print(0)
else:
    print(*unvisited,sep="\n")


