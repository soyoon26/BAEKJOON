import sys
n,l,r,x=map(int,sys.stdin.readline().split())
nums=list(map(int,sys.stdin.readline().split()))
nums.sort()
ans=[]
answer=0
def back(start):
    global answer
    if len(ans) >= 2:
        if l <= sum(ans) <= r:
            if max(ans)-min(ans)>= x:
                answer+=1
    for i in range(start,n):
        ans.append(nums[i])
        back(i+1)
        ans.pop()
back(0)
print(answer)