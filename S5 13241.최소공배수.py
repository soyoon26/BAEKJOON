A,B=map(int,input().split())
def gcd(a,b):
    while True:
        a,b=b,a%b
        if b == 0:
            break
    return a
print(A*B//gcd(A,B))