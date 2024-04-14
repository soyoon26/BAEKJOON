import sys
n = int(sys.stdin.readline().rstrip())
conference  = list(list(map(int,sys.stdin.readline().split())) for _ in range(n))
conference.sort(key = lambda x:(x[1],x[0]))
cnt=1

end = conference[0][1]
for i in range(1,n):
    if end <= conference[i][0]:
        cnt+=1
        end=conference[i][1]
print(cnt)