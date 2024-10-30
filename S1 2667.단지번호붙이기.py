import sys
n = int(sys.stdin.readline().rstrip())
town = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]

visited=[[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0] #좌우
dy = [0, 0, -1, 1] #상하

def dfs(x,y):
    visited[x][y] = True
    count = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and town[nx][ny]:
            count += dfs(nx,ny)
    return count

answer=[]

for i in range(n):
    for j in range(n):
        if town[i][j] == 1 and not visited[i][j]:
            cnt = dfs(i,j)
            answer.append(cnt)
answer.sort()
print(len(answer))
print(*answer,sep='\n')
