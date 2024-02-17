import sys
n,k=map(int,sys.stdin.readline().split())
dp=[1,2,1]
answer=[]
m=3
if n <3:
    print(1)
else:
    while m != n:
        m+=1
        for i in range(m):
            if i == 0:
                answer.append(1)
            elif i == m-1:
                answer.append(1)
            else:
                answer.append(dp[i-1]+dp[i])
        dp=answer[:]
        answer=[]
    print(dp[k-1])
