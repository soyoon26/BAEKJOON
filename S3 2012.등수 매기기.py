import sys
n = int(sys.stdin.readline().rstrip())
wish = list(int(sys.stdin.readline().rstrip()) for _ in range(n))
wish.sort()
cnt=0
for i in range(n):
    cnt += abs(wish[i]-(i+1))
print(cnt)