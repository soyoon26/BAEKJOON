import sys
n = int(sys.stdin.readline().rstrip())
nums = list(map(int,sys.stdin.readline().split()))
sum = [0]*(n)
sum[0] = nums[0]
for i in range(1,n):
    sum[i] = max(sum[i-1]+nums[i],nums[i])
print(max(sum))

