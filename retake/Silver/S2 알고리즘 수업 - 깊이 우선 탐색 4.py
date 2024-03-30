import sys
sys.setrecursionlimit(10**9)
N, M, R = map(int,sys.stdin.readline().split())
graph=[[] for _ in range(N+1)]
visited = [-1]*(N+1)

for _ in range(M):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

deapth = 0
def dfs(v,deapth):
    visited[v] = deapth
    graph[v].sort(reverse=True)
    for i in graph[v]:
        if visited[i] == -1:
            dfs(i,deapth+1)
dfs(R,0)
print(*visited[1:],sep='\n')

# sys.setrecursionlimit(10**9)만 다르게 풀었었는데 저번보다 시간이 줄었다..?