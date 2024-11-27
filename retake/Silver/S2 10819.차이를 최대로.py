import sys
from itertools import permutations
N = int(sys.stdin.readline().rstrip())
num=map(int, sys. stdin.readline().split())
per = list(permutations(num,N))
answer=0
for i in per:
    ans=0
        for j in range (N-1):
            ans+=abs(ilj]-i[j+1])
        if ans > answer:
            answer=ans
print(answer)
