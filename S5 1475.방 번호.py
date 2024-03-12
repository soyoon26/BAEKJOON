num=list(map(int,list(input())))
ans=[0]*10
for i in num:
    if i == 9:
        ans[6]+=1
    else: ans[i]+=1
if ans[6]>1:
    if ans[6]%2:
        ans[6]=ans[6]//2+1
    else:
        ans[6]=ans[6]//2
print(max(ans))