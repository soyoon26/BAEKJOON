import sys
input = sys.stdin.readline
H, W, X, Y = map(int,input().split())
B = list(list(map(int,input().split())) for _ in range(H + X))

for i in range(X,X+H):
    for j in range(Y,Y+W):
        B[i][j] -= B[i-X][j-Y]
for i in range(H):
    for j in range(W):
        print(B[i][j], end=" ")
    print()
