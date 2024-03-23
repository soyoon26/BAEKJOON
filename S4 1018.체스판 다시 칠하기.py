import sys
N,M=map(int,sys.stdin.readline().split())
board=[]
for i in range(N):
    board.append(list(sys.stdin.readline().rstrip()))
candi=[]

for a in range(N-7):
    for b in range(M-7):
        ans1 = 0
        ans2 = 0
        for i in range(a, a + 8):  # 행
            for j in range(b, b + 8):  # 열
                if (i + j) % 2 == 0:
                    if board[i][j] == 'W':
                        ans1 += 1
                    else:
                        ans2 += 1
                elif (i + j) % 2 == 1:
                    if board[i][j] == 'B':
                        ans1 += 1
                    else:
                        ans2 += 1

        candi.append(min(ans1,ans2))
print(min(candi))

# 이전 코드, N 실수
board=[]
for i in range(N):
    board.append(list(sys.stdin.readline().rstrip()))
candi=[]
def check(a,b,x,y):
    global candi
    point = 0
    for i in range(a,a+8): #행
        for j in range(b,b+8): #열
            if (i + j) % 2 == 0:
                if board[i][j] == x :
                    point += 1
            elif (i + j) % 2 == 1:
                if board[i][j] == y :
                    point +=1
    candi.append(point)
for i in range(N-7):
    for j in range(M-7):
        check(i,j,'W','B')
        check(i,j,'B','W')

print(min(candi))