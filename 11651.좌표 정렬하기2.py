N = int(input())
board = []

for i in range(N):
    x,y=map(int,input().split())
    board.append([y,x])

board.sort()
for i in range(N):
    print(board[i][1],board[i][0])