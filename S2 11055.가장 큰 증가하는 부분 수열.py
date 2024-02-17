import sys
N=int(sys.stdin.readline().rstrip())
num=list(map(int,sys.stdin.readline().split()))
dp=num[:] #또는 .copy
for i in range(N):
    for j in range(i):
        if num[i]>num[j]:
            if num[i]+dp[j]>dp[i]:
                dp[i]=num[i]+dp[j]
print(max(dp))

#반례
#3
#5 1 5

#작은 값이 없을 때 본인이 미리 들어가 있어야 한다. 