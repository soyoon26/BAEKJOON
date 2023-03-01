import sys
N = int(sys.stdin.readline())
paper = [[0 for i in range(1001)] for _ in range(1001)]
for p in range(1, N+1):
    a, b, w, h = map(int,sys.stdin.readline().split())
    for x in range(a,a+w):
        for y in range(b,b+h):
            paper[x][y] = p

for p in range(N):
    cnt = 0
    for i in range(1001):
        for j in range(1001):
            if paper[i][j] == p+1:
                cnt += 1
    print(cnt)