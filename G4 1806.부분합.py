import sys
N,S=map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))

n = len(nums)
start, end = 0,0
sum = 0
ans = []
while True:
    if sum >= S:
        ans.append(end-start)
        sum-=nums[start]
        start+=1
    elif end == N:
        break
    else:
        sum += nums[end]
        end += 1

if len(ans)>0:
    print(min(ans))
else:
    print(0)