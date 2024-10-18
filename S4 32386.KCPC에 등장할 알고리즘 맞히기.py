import sys
from collections import defaultdict
tags_dict = defaultdict(int)
n = int(input().rstrip())
for i in range(n):
    _, _, *tags = sys.stdin.readline().rstrip().split()
    for tag in tags:
        tags_dict[tag]+=1

max_value = max(tags_dict.values())
max_count = list(tags_dict.values()).count(max_value)

if max_count > 1:
    print(-1)
else:
    max_tag = max(tags_dict, key=tags_dict.get)
    print(max_tag)