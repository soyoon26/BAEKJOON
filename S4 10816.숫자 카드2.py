import sys
N = sys.stdin.readline().rstrip()
SG = list(sys.stdin.readline().rstrip().split())
M = sys.stdin.readline().rstrip()
num = list(sys.stdin.readline().rstrip().split())
SG_dict={}
ans=[]
for i in SG:
    if i in SG_dict:
        SG_dict[i]+=1
    else:
        SG_dict[i]=1
for j in num:
    if j in SG_dict:
        ans.append(SG_dict[j])
    else:
        ans.append(0)
print(*ans)