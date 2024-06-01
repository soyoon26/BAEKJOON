import sys
from collections import defaultdict
n = int(sys.stdin.readline().rstrip())
cnt=defaultdict(int)
for _ in range(n):
    name,file = sys.stdin.readline().rstrip().split('.')
    cnt[file]+=1
lst=list(cnt.keys())
lst.sort()
for i in lst:
    print(i,cnt[i])