K=int(input())
for k in range(1,K+1):
    print('Class',k)
    n,*score = list(map(int,input().split()))
    score.sort()
    gap=0
    for i in range(1,n):
        if gap < score[i]-score[i-1]:
            gap = score[i]-score[i-1]
    print(f"Max {score[-1]}, Min {score[0]}, Largest gap {gap}")
