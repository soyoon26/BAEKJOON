import sys
n=int(sys.stdin.readline().rstrip())
num=list(map(int,sys.stdin.readline().split()))
X=int(sys.stdin.readline().rstrip())
i,j=0,n-1
num.sort()
cnt=0
while i < j:
    sum = num[i]+num[j]
    if sum < X:
        i+=1
    elif sum > X:
        j-=1
    else:
        cnt+=1
        i+=1
        j-=1
print(cnt)

#2
#1 2
#13