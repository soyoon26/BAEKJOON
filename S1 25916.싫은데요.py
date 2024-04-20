import sys
n,m = map(int,sys.stdin.readline().split())
#뚫린 구멍 수, 햄스터 부피
holes = list(map(int,sys.stdin.readline().split()))
#구멍
start, end, ans = 0,0,0
ham = 0
while end < n+1:
    if ham > m: #햄스터 부피보다 커지면
        ham-=holes[start]
        start+=1
    else:
        ans = max(ham, ans)
        if end == n:
            break
        ham+=holes[end]
        end+=1
print(ans)
