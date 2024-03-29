import sys
N, M = map(int,sys.stdin.readline().split())
num = list(map(int,sys.stdin.readline().split()))
num.sort()
answer = []
def back(start):
    if len(answer) == M:
        print(*answer)
        return
    for i in range(start,len(num)):
            answer.append(num[i])
            back(i)
            answer.pop()

back(0)