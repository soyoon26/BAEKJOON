import sys
T=int(sys.stdin.readline().rstrip())

for t in range(T):
    N=int(sys.stdin.readline().rstrip())
    fashion = dict()
    for n in range(N):
        item=sys.stdin.readline().split()
        if item[1] in fashion:
            fashion[item[1]]+=1
        else:
            fashion[item[1]]=1

    total_comb=1
    for cnt in fashion.values():
        total_comb *= (cnt+1) #안 입었을 수도 있는 상황
    print(total_comb-1) #알몸이 상태 제외
