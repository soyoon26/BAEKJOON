N , K = map(int,input().split())
ans = 1
ans2 =1
if K == 0:
    print(1)
else:
    for i in range(1,K+1):
        ans *= N
        N -= 1
        ans2 *= i
    print(int(ans/ans2))
