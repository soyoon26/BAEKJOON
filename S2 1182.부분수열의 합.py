import sys
from itertools import combinations
n, s = map(int,sys.stdin.readline().split())
nums=list(map(int,sys.stdin.readline().split()))
answer=0
for i in range(1,n+1):
    lst=list(combinations(nums,i))
    for j in lst:
        if s == sum(j):
            answer+=1
print(answer)