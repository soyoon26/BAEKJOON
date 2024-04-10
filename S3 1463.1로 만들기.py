import sys
x = int(sys.stdin.readline().rstrip())
dp = [0]*(x+3)
dp[2], dp[3] = 1,1
for i in range(4,x+1):
    dp[i] = dp[i-1]+1
    if i%3 == 0:
        dp[i] = min(dp[i],dp[i//3]+1)
    if i%2 == 0:
        dp[i] = min(dp[i],dp[i//2]+1)

print(dp[x])