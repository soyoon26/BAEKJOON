import math
n=int(input())
ans=math.ceil(n**(0.5))
if ans**2 >= n:
    print(ans)
else:
    print(ans+1)