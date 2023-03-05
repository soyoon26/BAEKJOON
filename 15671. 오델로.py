from pprint import pprint
N = int(input())
board = [['.' for i in range(6)]for _ in range(6)]
board[2][2] = 'W'
board[3][3] = 'W'
board[2][3] = 'B'
board[3][2] = 'B'

W_cnt = 0
B_cnt = 0

di = [-1,-1,-1,0,0,1,1,1]
dj = [-1,0,1,-1,1,-1,0,1]

def othello(N,R,C):
    if N%2:#짝수면 흑 홀수면 백
        num = 'W'
    else:
        num = 'B'  #판 조회
    board[R-1][C-1] = num #놓은 돌 바꿔주기
    for k in range(8):  #di,dj범위
        lst = []
        for l in range(1,6): # 주변 탐색
            dx = R-1 + di[k]*l
            dy = C-1 + dj[k]*l
            if 0 <= dx < 6 and 0 <= dy < 6: #범위 제한
                if board[dx][dy] == '.':
                    break
                elif board[dx][dy] != num:
                    lst.append([dx,dy])
                else:
                    while lst:
                        x,y = lst.pop()
                        board[x][y] = num
                    break


for i in range(N):
    R, C = map(int,input().split())
    othello(i,R,C)
for j in range(6):
    for k in range(6):
        if board[j][k] == 'W':
            W_cnt += 1
        elif board[j][k] == 'B':
            B_cnt += 1

for i in range(6):
    print(''.join(board[i]))
if W_cnt > B_cnt :
    print('White')
else:
    print('Black')