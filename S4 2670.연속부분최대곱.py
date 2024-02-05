import sys
N=int(sys.stdin.readline().rstrip())
lst=[float(input()) for _ in range(N)]
for i in range(1,N):
    lst[i] = max(lst[i],lst[i]*lst[i-1])
print('%0.3f' % max(lst))

#지금까지 곱해온 값을 저장