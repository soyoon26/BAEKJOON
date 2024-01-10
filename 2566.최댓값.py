board = [list(map(int,input().split())) for _ in range(9)]
max=0
row=0
column=0
for i in range(9):
    for j in range(9):
        if board[i][j] >= max:
            max=board[i][j]
            row=i+1
            column=j+1
print(max)
print(row,column)
#다른 방법 : 행렬.index(해당숫자)