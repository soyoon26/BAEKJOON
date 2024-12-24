n=int(input())
d={}
for i in range(n):
    s=input()
    if s not in d:
        d[s]=1
    else:
        d[s]+=1
max=0
for i in d:
    if d[i]>max:
        max=d[i]
        ans=i
    elif d[i]==max and ans>i:
        ans=i
