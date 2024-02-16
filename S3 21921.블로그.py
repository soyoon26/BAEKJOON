import sys
N,X=map(int,sys.stdin.readline().split())
num=list(map(int,sys.stdin.readline().split()))
sum=[sum(num[:X])]
for i in range(N-X):
    sum.append(sum[i]+num[i+X]-num[i])
ans=max(sum)
if ans == 0:
    print('SAD')
else:
    print(ans)
    print(sum.count(ans))



