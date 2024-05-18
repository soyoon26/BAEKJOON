import sys
from collections import defaultdict
names = defaultdict(int)

while True:
    name = sys.stdin.readline().rstrip()
    if not name:
        break
    names[name]+=1
tree=list(names.keys())
tree.sort()

total = sum(names.values())
for i in tree:
    print('%s %.4f' %(i,(names[i]/total)*100))