import sys
N=int(sys.stdin.readline().rstrip())
nums=list(map(int,sys.stdin.readline().split()))
def long(lst,n):
    ans=0
    cnt=0
    for i in range(1,n):
        if lst[i]>=lst[i-1]:
            cnt+=1
        else:
            if ans < cnt:
                ans=cnt
            cnt=0
    if ans < cnt:
        ans=cnt
    return ans+1
print(max(long(nums,N),long(nums[::-1],N)))