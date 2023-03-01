import sys
N = int(input())
paper = [[]for i in range(N)]
for p in range(N):
    a, b, w, h = map(int,sys.stdin.readline().split())
    for x in range(a,a+w):
        for y in range(b,b+h):
            paper[p].append((x,y))

for i in range(N):
    for j in range(i+1,N):
        for k in paper[j]:
            try:
                paper[i].remove(k)
            except:
                pass
    print(len(paper[i]))
