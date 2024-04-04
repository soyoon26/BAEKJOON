import sys
A = int(sys.stdin.readline().rstrip())
Ai = list(map(int,sys.stdin.readline().split()))
dp = [1]*A

for i in range(A):
    for j in range(i):
        if Ai[i] > Ai[j]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))