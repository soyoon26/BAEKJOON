import sys
n = int(sys.stdin.readline().rstrip())
dp = [0]*(n+2)
dp[1], dp[2] = 1,2
for i in range(3,n+1):
    dp[i] = (dp[i-2] + dp[i-1])%15746
print(dp[n])

# 메모리초과로 인해 dp배열에서 부터 나눠줘야 함
# 4는 2에 00을 붙이고 3에 1을 붙여주면 됨