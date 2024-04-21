import sys
n,k = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))

start, end = 0,0
cnt, ans= 0, 0

while end < n:

    if cnt <= k:
        if nums[end]%2:
            cnt+=1
        else: #k인 경우 짝수를 더할 때
            ans = max(ans, end - start - cnt + 1)
        end+=1
    else:
        if nums[start]%2:
            cnt-=1
        start+=1
print(ans)