import sys
N,S=map(int,sys.stdin.readline().split())
cows=[]
for i in range(N):
    cow=int(sys.stdin.readline().rstrip())
    cows.append(cow)
cows.sort()
i,j=0,N-1
cnt=0
while i < j:
    if cows[i]+cows[j] <= S:
        cnt+=j-i
        i+=1
    else:
        j-=1
print(cnt)