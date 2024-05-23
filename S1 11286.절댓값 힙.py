import sys, heapq
from collections import defaultdict
n=int(sys.stdin.readline().rstrip())
nums=[]
numd=defaultdict(int)
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    numd[num] += 1
    if num < 0:
        heapq.heappush(nums,-num)
    elif num > 0:
        heapq.heappush(nums,num)
    else:
        if nums:
            np = heapq.heappop(nums)
            if numd[-np] > 0:
                numd[-np] -= 1
                print(-np)
            else:
                numd[np] -= 1
                print(np)
        else:
            print(0)

#다른 풀이 - 절댓값, 원래값 함께 저장
import sys
input = sys.stdin.readline
import heapq

hq = []

for _ in range(int(input())):
    n = int(input())
    if n == 0:
        if hq:
            print(heapq.heappop(hq)[1])
        else:
            print(0)
    else:
        heapq.heappush(hq, (abs(n), n))