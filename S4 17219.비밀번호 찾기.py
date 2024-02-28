import sys
N,M=map(int,sys.stdin.readline().split())
dict=dict()
for i in range(N):
    site,pw=sys.stdin.readline().split()
    dict[site]=pw
for j in range(M):
    site=sys.stdin.readline().rstrip()
    print(dict[site])