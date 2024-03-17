import sys
cnt=1
while True:
    n= int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    lst=list(sys.stdin.readline().rstrip() for _ in range(n))
    ear = list(0 for _ in range(n))
    for i in range(n*2-1):
        number=sys.stdin.readline().split()
        ear[int(number[0])-1]+=1
    ans=[idx for idx,value in enumerate(ear) if value == 1]
    print(cnt,lst[ans[0]])
    cnt+=1

#remove, append
