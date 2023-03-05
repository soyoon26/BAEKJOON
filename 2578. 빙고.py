
board = [list(map(int,input().split())) for _ in range(5)]
MC = [list(map(int,input().split())) for _ in range(5)]

di = [0,1,1,1]
dj = [1,-1,0,1]

def bingo():
    global bingo_cnt
    bingo_cnt = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] == 0:
                for k in range(4):
                    num_cnt = 0
                    for l in range(5): #범위 지정
                        dx = i + di[k]*l
                        dy = j + dj[k]*l

                        if 0 <= dx < 5 and 0 <= dy < 5:
                            if board[dx][dy] == 0:
                                num_cnt += 1
                                if num_cnt == 5:
                                    bingo_cnt += 1


flag = 0

for i in range(5):
    for j in range(5):
        num = MC[i][j]
        for k in range(5):
            for l in range(5):
                if board[k][l] == num:
                    board[k][l] = 0
                    bingo()
                    if bingo_cnt >= 3:
                        print(i*5+j+1)
                        flag = 1
                        break

                if flag == 1:
                    break
            if flag == 1:
                break
        if flag == 1:
            break
    if flag == 1:
        break
