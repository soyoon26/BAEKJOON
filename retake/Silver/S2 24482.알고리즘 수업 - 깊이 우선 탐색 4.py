import sys
sys.setrecursionlimit(10**9)
n, m, r = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [-1]*(n+1)
for i in range(m):
    u, v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(v,cnt):
    visited[v] = cnt
    graph[v].sort(reverse=True)
    for i in graph[v]:
        if visited[i] == -1:
            dfs(i,cnt+1)

dfs(r,0)
print(*visited[1:],sep='\n')