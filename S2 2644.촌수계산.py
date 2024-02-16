from collections import deque
import sys

n=int(sys.stdin.readline())
a,b=map(int,sys.stdin.readline().split())
m=int(sys.stdin.readline())
graph = [[]for _ in range(n+1)]
visited=[]
ans=[0]*(n+1)
for i in range(m):
    x,y= map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(a,b):
    queue=deque([a])
    visited.append(a)
    while queue:
        V=queue.popleft()
        for j in graph[V]:
            if j not in visited:
                if j == b:
                    visited.append(j)
                    print(ans[V]+1)
                    break
                queue.append(j)
                visited.append(j)
                ans[j]=ans[V]+1

bfs(a,b)
if b not in visited:
    print(-1)