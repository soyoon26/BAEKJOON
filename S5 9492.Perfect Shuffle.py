import sys
while True:
    N=int(sys.stdin.readline().rstrip())
    if N == 0:
        break
    cards=[sys.stdin.readline().rstrip() for _ in range(N)]
    if N%2:
        for i in range(N//2+1):
            if i != N//2:
                print(cards[i],cards[i+N//2+1],sep='\n')
            else:
                print(cards[i])
    else:
        for i in range(N//2):
            print(cards[i],cards[i+N//2],sep='\n')

#다른 방법
ip = sys.stdin.readline
pt = sys.stdout.write
while True:
    n = int(ip())
    if n==0:
        break
    li = []
    for _ in range(n):
        li.append(ip().rstrip())
    a,b = li[:(n//2)+(n%2)],li[(n//2)+(n%2):]
    for _ in range(n//2):
        pt(f"{a[_]}\n")
        pt(f"{b[_]}\n")
    if n%2==1:
        pt(f"{a[-1]}\n")