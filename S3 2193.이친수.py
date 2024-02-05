N=int(input())
zero=[0,1,1]+[0]*(N-3)
one=[1,0,1]+[0]*(N-3)

for i in range(3,N):
    zero[i]=zero[i-1]+one[i-1]
    one[i]=zero[i-1]
print(zero[N-1]+one[N-1])

#더 간단한 방법
N=int(input())
dp=[0 for _ in range(N+1)]
dp[1]=1
for n in range(2,N+1):
    dp[n]=dp[n-1]+dp[n-2]
print(dp[N])