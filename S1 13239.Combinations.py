import math, sys
t=int(sys.stdin.readline().rstrip())
for _ in range(t):
    n,k=map(int,sys.stdin.readline().split())
    num=math.factorial(n)//(math.factorial(k)*math.factorial(n-k))
    print(num%(10**9+7))
