import math
def gcd(a,b):
    while b != 0:
        a,b=b,a%b
    return a
N=int(input())
n_lst=list(map(int,input().split()))
M=int(input())
m_lst=list(map(int,input().split()))
ans=str(gcd(math.prod(n_lst),math.prod(m_lst)))
if len(ans)>9:
    print(ans[-9:])
else:
    print(ans)