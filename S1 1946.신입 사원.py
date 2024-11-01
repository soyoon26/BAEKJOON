import sys
input = sys.stdin.readline
T = int(input().rstrip())
for t in range(T):
    N = int(input().rstrip())
    rank = list(list(map(int,input().split())) for _ in range(N))
    rank.sort()
    answer = 0
    min = N + 1
    for i in range(N):
        if rank[i][1] < min:
            min = rank[i][1]
            answer+=1
    print(answer)