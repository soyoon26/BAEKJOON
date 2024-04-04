import sys
N = int(sys.stdin.readline().rstrip())
candi = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
og_me=candi[0]
me = candi[0]
candi=candi[1:]

if N > 1:
    while max(candi) >= me:
        candi.sort(reverse=True)
        candi[0]-=1
        me+=1
    print(me-og_me)
else:
    print(0)