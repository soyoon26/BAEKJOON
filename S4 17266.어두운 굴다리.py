import sys, math
N = int(sys.stdin.readline().rstrip()) #굴다리 길이
M = int(sys.stdin.readline().rstrip()) #가로등 개수
x = list(map(int,sys.stdin.readline().split())) #가로등 위치

answer= [N-x[-1],x[0]]
for i in range(1,M):
    answer.append((x[i]-x[i-1])/2)
if max(answer)%1:
    print(math.ceil(max(answer)))
else:
    print(int(max(answer)))