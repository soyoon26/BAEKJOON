from itertools import permutations

N,M = map(int,input().split())
num=list(range(1,N+1))
cb = list(permutations(num,M))
for i in cb:
    print(*i)