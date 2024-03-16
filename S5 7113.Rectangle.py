import sys
sys.setrecursionlimit(10**6)
n,m=map(int,input().split())

cnt=0
def rectangle(n,m):
    global cnt
    if n == m:
        cnt+=1
        print(cnt)
        return cnt
    else:
        if n>m:
            cnt+=1
            rectangle(n-m,m)
        else:
            cnt+=1
            rectangle(n,m-n)
rectangle(n,m)


#다른 방법
N,M=map(int,input().split())

cnt=1 #마지막에 같을 때

width=N
length=M

while width!=length:
    if width>length:
        width-=length
    else:
        length-=width
    cnt+=1

print(cnt)