import sys
N, taesoo, P = map(int,sys.stdin.readline().split())
answer=-1
if N > 0:
    score=list(map(int,sys.stdin.readline().split()))
    score.sort(reverse=True)
    rank=1
    cnt=1
    for i in score:
        if i>taesoo :
            rank+=1
            cnt+=1
        elif i==taesoo:
            cnt+=1
        elif i<taesoo:
            break
    if cnt > P:
        print(-1)
    else:
        print(rank)
else:
    print(1)
