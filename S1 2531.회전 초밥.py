import sys
from collections import defaultdict
n, d, k, c = map(int,sys.stdin.readline().split())
#접시수, 초밥가짓수, 연속먹는 접시수, 쿠폰번호
sushi = list(int(sys.stdin.readline().rstrip()) for _ in range(n))

start, end = 0, k
eat=defaultdict(int)
ans=[]
for i in range(start,end):
    eat[sushi[i]] += 1
eat[c] += 1

while start<n:
    ans.append(len(eat))
    eat[sushi[start]] -= 1
    if eat[sushi[start]] == 0:
        del eat[sushi[start]]
    eat[sushi[end%n]] += 1
    start+=1
    end+=1

print(max(ans))