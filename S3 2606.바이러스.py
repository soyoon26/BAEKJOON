M=int(input())
N=int(input())
graph = [[] for _ in range(M+1)]
for i in range(N):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[]
def dfs(v):
    visited.append(v)
    for j in graph[v]:
        if j not in visited:
            dfs(j)
dfs(1)
print(len(visited)-1)