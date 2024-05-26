import sys
n=int(sys.stdin.readline().rstrip())
nums=list(map(int,sys.stdin.readline().split()))
dp=[0]*n
buy=nums[0]
earn = 0
for i in range(n):
    if buy > nums[i]:
        buy = nums[i]
    else:
        if nums[i]-buy > earn:
            earn = nums[i]-buy
print(earn)