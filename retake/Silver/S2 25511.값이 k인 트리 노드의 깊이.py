import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, k = map(int,input().split())
graph=[[] for i in range(n)]

for i in range(n-1):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
nodes = list(map(int,input().split()))
visited=[False]*n

def dfs(start,cnt):
    if nodes[start] == k:
        print(cnt)
        exit()
    for j in graph[start]:
        if not visited[j]:
            visited[j] = True
            dfs(j,cnt+1)
            visited[j] = False
visited[0] = True
ans = dfs(0,0)