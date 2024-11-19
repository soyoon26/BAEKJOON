import sys
input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))

S.sort()
target = 1
for num in S:
    if num > target:
        break
    target += num
print(target)
