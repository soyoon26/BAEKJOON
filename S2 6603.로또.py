import sys
ans=[]
def back(arr, k, idx):
    if len(ans) == 6:
        print(*ans)
        return
    for i in range(idx,k):
        if S[i] not in ans:
            ans.append(S[i])
            back(arr,k,i+1)
            ans.pop()
    return
while True:
    k, *S= list(map(int,sys.stdin.readline().split()))
    if k == 0:
        break
    back(S,k,0)
    print()


