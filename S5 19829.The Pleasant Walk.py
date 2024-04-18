import sys
n, k= map(int,sys.stdin.readline().split())
colors = list(map(int,sys.stdin.readline().split()))
ans=[1]
cnt = 0
for i in range(1,n):
    if colors[i-1] != colors[i]:
      cnt+=1
    elif colors[i-1] == colors[i]:
        ans.append(cnt+1)
        cnt=0
    if i == n-1:
        ans.append(cnt+1)
print(max(ans))