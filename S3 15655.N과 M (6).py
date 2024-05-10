import sys
n,m= map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))
nums.sort()
ans=[]
def back(start):
    if len(ans) == m:
        print(*ans)
        return
    for i in range(start,n):
        if nums[i] not in ans:
            ans.append(nums[i])
            back(i+1)
            ans.pop()
back(0)