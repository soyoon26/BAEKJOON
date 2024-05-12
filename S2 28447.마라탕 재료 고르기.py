import sys
n,k=map(int,sys.stdin.readline().split())
nums = list(list(map(int,sys.stdin.readline().split())) for _ in range(n))
ans = []
ks = list(range(n))
ans=[]
sums=[]
def back(start):
    if len(ans)==k:
        answer = 0
        for i in range(k):
            for j in range(i + 1, k):
                answer+=nums[ans[i]][ans[j]]
        sums.append(answer)
        return
    for i in range(start,n):
        if ks[i] not in ans:
            ans.append(ks[i])
            back(i+1)
            ans.pop()
back(0)
print(max(sums))

