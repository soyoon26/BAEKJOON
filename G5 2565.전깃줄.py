import sys
n = int(sys.stdin.readline().rstrip())
wires = list(list(map(int,sys.stdin.readline().split())) for _ in range(n))
wires.sort(key = lambda x:x[0])

num = [0]*501
for i,j in wires:
    num[j] = max(num[:j]) + 1

print(n-max(num))
