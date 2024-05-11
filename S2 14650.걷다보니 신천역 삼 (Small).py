import sys
nums=[0,1,2]
n = int(sys.stdin.readline().rstrip())
ans=[]
answer=0
def back():
    global answer
    if len(ans) == n :
        res = int(''.join(map(str,ans)))
        if res % 3 == 0:
            answer+=1
        return
    for i in nums:
        if len(ans) == 0 and i == 0:
            continue
        ans.append(i)
        back()
        ans.pop()
back()
print(answer)