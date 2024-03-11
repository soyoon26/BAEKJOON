import sys
N=int(sys.stdin.readline().rstrip())
words=list(set(sys.stdin.readline().rstrip() for _ in range(N)))
n=len(words)

ans=0
for i in range(n):
    cnt=0
    for j in range(n):
        if words[i] != words[j]:
            if words[j].startswith(words[i]):
                break
            else:
                cnt+=1
    if cnt==n-1:
        ans+=1
print(ans)