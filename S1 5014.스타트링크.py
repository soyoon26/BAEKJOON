import sys
from collections import deque
F, S, G, U, D = map(int, sys.stdin.readline().split())
visited = [False]*(F+1)
def bfs(start):
    queue = deque([(start,0)])
    visited[start] = True
    while queue:
        current, cnt = queue.popleft()
        if current == G:
            return cnt
        if current + U <= F and not visited[current + U]:
            visited[current + U] = True
            queue.append((current + U, cnt + 1))
        if current - D >= 1 and not visited[current - D]:
            visited[current - D] = True
            queue.append((current - D, cnt + 1))
    return "use the stairs"

answer = bfs(S)
print(answer)