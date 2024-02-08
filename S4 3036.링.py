def gcd(a,b):
    while b != 0:
        a,b=b,a%b
    return a
N=int(input())
n,*num=list(map(int,input().split()))
for i in range(len(num)):
    gcd_n=gcd(n,num[i])
    print(f'{n//gcd_n}/{num[i]//gcd_n}')
