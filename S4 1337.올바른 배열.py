import sys
N=int(sys.stdin.readline())
lst=[]
for n in range(N):
    num=int(sys.stdin.readline().rstrip())
    lst.append(num)
lst.sort()
number=0
count=[]
for i in range(len(lst)):
    number=list(range(lst[i],lst[i]+5))
    cnt=0
    for j in range(i,len(lst)):
        if lst[j] in number:
            cnt+=1
    count.append(cnt)
count.sort(reverse=True)
if count[0]>=5:
    print(0)
else:
    print(5-count[0])
#없으면 cnt를 세는게 낫다. 그러고 min을 구하기