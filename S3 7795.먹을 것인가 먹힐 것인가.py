import sys
import bisect
input = sys.stdin.readline
T = int(input())
for t in range(T):
    cnt = map(int,input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()
    ans = 0
    for i in a:
        ans += bisect.bisect_left(b,i)
    print(ans)

