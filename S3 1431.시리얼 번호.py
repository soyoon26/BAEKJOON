import sys
N=int(sys.stdin.readline().rstrip())
lst=[]
for i in range(N):
    guitar=sys.stdin.readline().rstrip()
    lst.append(guitar)
lst.sort(key=lambda x: (len(x),sum(int(c) for c in x if c.isdigit()),x))
print(*lst,sep='\n')