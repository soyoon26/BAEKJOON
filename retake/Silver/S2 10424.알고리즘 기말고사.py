import sys
N = int(input())
ans=[0]*N
final = list(map(int,sys.stdin.readline().split()))
for i in range(N):
    ans[i]=final.index(i+1)+1
    print((i+1)-ans[i])
