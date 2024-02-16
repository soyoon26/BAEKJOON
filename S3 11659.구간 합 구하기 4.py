import sys
N,M=map(int,sys.stdin.readline().split())
num=list(map(int,sys.stdin.readline().split()))
sum=[num[0]]+[0]*N
for i in range(1,N):
    sum[i]=sum[i-1]+num[i]
for i in range(M):
    i,j=map(int,sys.stdin.readline().split())
    print(sum[j-1]-sum[i-2])