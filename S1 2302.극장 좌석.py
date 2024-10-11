n = int(input())
m = int(input())
vip = list(int(input()) for i in range(m))
# n-m 자리는 최대로 있을 수 있음
can = [i for i in range(n-m+10)]
can[0] = 1
can[1] = 1
can[2] = 2
for i in range(3,n-m+1):
    can[i] = can[i-1] + can[i-2]
cnt, ans = 0, 1
for i in range(1,n+1):
    if i in vip:
        ans *= can[cnt]
        cnt = 0
    else:
        cnt+=1
if cnt > 0:
    ans*=can[cnt]
print(ans)