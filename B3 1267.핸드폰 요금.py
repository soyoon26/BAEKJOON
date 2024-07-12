import sys
n = int(sys.stdin.readline().rstrip())
call = map(int,sys.stdin.readline().split())
m = 0
y = 0
for i in call:
    y += (i // 30 + 1)*10
    m += (i // 60 + 1)*15
if m == y:
    print("Y M",y)
elif m < y:
    print("M",m)
else:
    print("Y",y)