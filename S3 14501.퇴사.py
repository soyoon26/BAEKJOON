import sys
input = sys.stdin.readline
n = int(input())
lst = [tuple(map(int, input().split())) for _ in range(n)]
dp = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    time, pay = lst[i]
    if i + time <= n:
        dp[i] = max(pay + dp[i + time], dp[i + 1])
    else:
        dp[i] = dp[i + 1]

print(dp[0])
