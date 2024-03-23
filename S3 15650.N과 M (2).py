import sys
from itertools import combinations

N,M=map(int,sys.stdin.readline().split())
lst=list(range(1,N+1))
for i in list(combinations(lst,M)):
    print(*i)