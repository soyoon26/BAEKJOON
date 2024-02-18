import sys
N, M = map(int,sys.stdin.readline().split())
num = list(map(int,sys.stdin.readline().split()))
cnt=0
i,j=0,1
while i <= j and j <=N :
    nums=num[i:j]
    sum_num=sum(nums)
    if sum_num < M:
        j+=1
    elif sum_num > M:
        i+=1
    else:
        cnt+=1
        i+=1
print(cnt)

#i==j가 되면 0값이 나와서 j+=1이 됨
