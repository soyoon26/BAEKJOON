T = int(input())

for tc in range(T):
    def Othello(player,x,y):
        board[x][y] = player
        di = [-1,-1,-1,0,0,1,1,1]
        dj = [-1,0,1,-1,1,-1,0,1]
        for i in range(8):
            for j in range(2,N):
                dx = x + di[i]*j
                dy = y + dj[i]*j
                if 0 <= dx < N+2 and 0 <= dy < N+2:
                    if board[dx][dy] == player:

                        cnt = 0
                        cnt_1 = 0
                        for k in range(1,j):
                            if board[x + di[i] * k][y + dj[i] * k] == 0:
                                cnt += 1
                                if cnt == 0 :
                                    board[x + di[i] * k][y + dj[i] * k] = player
                            elif board[x + di[i] * k][y + dj[i] * k] != 0 and board[x + di[i] * k][y + dj[i] * k] != player:
                                cnt_1 += 1
                                if cnt_1 == j-1:
                                    board[x + di[i] * k][y + dj[i] * k] = player


                                    for l in range(j+1):
                                        board[dx][dy] = player
                                        board[x + di[i] * l][y + dj[i] * l] = player


    N, M = map(int,input().split())  #M이 놓는 횟수

    board = [[0]+[0 for i in range(N)]+[0] for _ in range(N+2)]
    N2 = int(N/2)
    board[N2][N2] = 2
    board[N2][N2+1] = 1
    board[N2+1][N2] = 1
    board[N2+1][N2+1] = 2

    for i in range(M):
        y, x, player = map(int,input().split())
        Othello(player,x,y)

    cnt_w = 0
    cnt_b = 0
    for i in range(N+2):
        for j in range(N+2):
            if board[i][j] == 1:
                cnt_b += 1
            elif board[i][j] == 2:
                cnt_w += 1
    print(f'#{tc+1}',cnt_b,cnt_w)