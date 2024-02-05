import math
T=int(input())
for t in range(T):
    N, M = map(int,input().split())
    print(math.comb(M,N))

#시간 줄이기 구현, factorial 사용
for j in range(m):
  n=list(map(int,sys.stdin.readline().split()))
  ans=1
  for i in range(n[1],n[1]-n[0],-1):
    ans=ans*i
  print(int(ans/(math.factorial(n[0]))))