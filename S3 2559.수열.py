import sys
N,K=map(int,sys.stdin.readline().split())
temp=list(map(int,sys.stdin.readline().split()))
i=0
max=sum(temp[:K])
sum_temp=sum(temp[:K])
while i!=N-K:
    sum_temp=sum_temp-temp[i]+temp[i+K]
    if max < sum_temp:
        max=sum_temp
    i+=1
print(max)
