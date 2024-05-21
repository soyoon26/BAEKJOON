n = int(input())
nums = list(range(1,n+1))
ans=[]
def back():
    if len(ans) == n:
        print(*ans)
    for i in nums:
        if i not in ans:
            ans.append(i)
            back()
            ans.pop()
back()
