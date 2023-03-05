board = [[0 for i in range(102)] for _ in range(102)]
N = int(input())
for i in range(N):
    x,y = map(int,input().split())
    for j in range(x+1,x+11):
        for k in range(y+1,y+11):
            board[j][k] = 1

di = [-1,1,0,0]
dj = [0,0,-1,1]
cnt = 0
for i in range(102):
    for j in range(102):
        for k in range(4):
            if 0 <= i+di[k] < 102 and 0 <= j+dj[k] < 102:
                if board[i][j] == 1 and board[i+di[k]][j+dj[k]] == 0:
                    cnt += 1

print(cnt)
