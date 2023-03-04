N = int(input()) #색종이 수
paper = []
for i in range(N):
    x,y = map(int,input().split())
    paper.append([x,y])

board = [[0 for i in range(100)] for _ in range(100)]
for k in range(N):
    for i in range(paper[k][0],paper[k][0]+10):
        for j in range(paper[k][1],paper[k][1]+10):
            board[i][j] = 1
cnt = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == 1:
            cnt+= 1
print(cnt)
