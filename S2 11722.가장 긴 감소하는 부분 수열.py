import sys
N=int(sys.stdin.readline().rstrip())
A=list(map(int,sys.stdin.readline().split()))
dp=[1]*(N)
for i in range(N):
    for j in range(i):
        if A[i]<A[j]:
            if dp[i]<dp[j]+1:
                dp[i]=dp[j]+1
print(max(dp))