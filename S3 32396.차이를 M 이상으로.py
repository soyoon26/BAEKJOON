import sys
n,m=map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))
answer = 0
for i in range(n-1):
    if abs(nums[i]-nums[i+1]) > m:
        continue
    elif abs(nums[i]-nums[i+1]) < m:
        nums[i+1] = -m
        answer += 1
print(answer)
