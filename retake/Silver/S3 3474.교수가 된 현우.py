import sys
T=int(input())
for t in range(T):
    num=int(sys.stdin.readline().rstrip())
    i=5
    cnt=0
    while i <= num:
        cnt += num // i
        i*=5
    print(cnt)
