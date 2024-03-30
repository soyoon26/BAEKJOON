import sys
n=int(sys.stdin.readline().rstrip())
m=int(sys.stdin.readline().rstrip())
graph=[[] for _ in range(n+1)]
for i in range(m):
    u,v=map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited=[False]*(n+1)
answer=0
def dfs(v):
    global answer
    visited[v] = True
    answer+=1
    for i in graph[v]:
        if visited[i] == False:
            dfs(i)
dfs(1)
if answer != 0:
    print(answer-1)
else:
    print(0)

# 저번에 더 짧고 빠르게 풀었다.. 충격
# visited에 없으면 append하면 됨.
# 이번에 감염된 컴퓨터가 없을 경우를 생각하여 조건으로 나누었는데 생각해보니 첫 시작도 1은 더해져서 상관없었다.
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