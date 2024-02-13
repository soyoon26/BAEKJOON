from collections import deque

N,M,v=map(int,input().split())

graph = [[False]*(N+1) for _ in range(N+1)]
visited_dfs = [False]*(N+1)
visited_bfs = [False]*(N+1)
for i in range(M):
    d1,d2=map(int,input().split())
    graph[d1][d2] = True
    graph[d2][d1] = True
def dfs(v):
    visited_dfs[v] = True
    print(v, end=" ")
    for i in range(1,N+1):
        if not visited_dfs[i] and graph[v][i]:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited_bfs[v] = True
    while queue:
        v = queue.popleft()
        print(v,end=" ")
        for i in range(1,N+1):
            if not visited_bfs[i] and graph[v][i]:
                queue.append(i)
                visited_bfs[i] = True
dfs(v)
print()
bfs(v)

#시간 줄이기
import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def bfs(node):
  queue = deque([node])
  answer_bfs.append(node)

  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if i not in answer_bfs:
        queue.append(i)
        answer_bfs.append(i)


def dfs(node):
  answer_dfs.append(node)

  for i in graph[node]:
    if i not in answer_dfs:
      dfs(i)

N,M,V = map(int, input().split())

graph =  [[] for _ in range(N+1)]

answer_dfs = []
answer_bfs = []

for i in range(M):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

for i in range(len(graph)):
  graph[i].sort()

dfs(V)
bfs(V)

print(" ".join(map(str, answer_dfs)))
print(" ".join(map(str, answer_bfs)))

