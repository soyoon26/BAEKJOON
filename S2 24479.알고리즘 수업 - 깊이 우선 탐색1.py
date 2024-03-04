import sys
sys.setrecursionlimit(150000)
N,M,R=map(int,sys.stdin.readline().split())
graph=[[] for i in range(N+1)]
visited=[0]*(N+1)
for m in range(M):
    u,v=map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
cnt=1
def dfs(graph,v,visited):
    global cnt
    visited[v]=cnt
    graph[v].sort()
    for i in graph[v]:
        if not visited[i]:
            cnt+=1
            dfs(graph,i,visited)
dfs(graph,R,visited)
for i in range(1,len(visited)):
    print(visited[i])
