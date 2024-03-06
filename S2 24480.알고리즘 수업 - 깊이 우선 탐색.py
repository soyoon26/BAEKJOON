import sys
sys.setrecursionlimit(10**8)
N,M,R=map(int,sys.stdin.readline().split())
visited=[False]*(N+1)
graph=[[] for i in range(N+1)]
for k in range(M):
    i,j=map(int,sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)
answer=[0]*(N)
order=1
def dfs(v):
    global order
    visited[v]=True
    answer[v-1]=order
    graph[v].sort(reverse=True)
    for i in graph[v]:
        if not visited[i]:
            order+=1
            dfs(i)
dfs(R)
print(*answer,sep='\n')