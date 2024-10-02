import sys
from collections import defaultdict
n,m = map(int,sys.stdin.readline().split())
memo = [sys.stdin.readline().rstrip() for _ in range(n)]
blog = [list(sys.stdin.readline().rstrip().split(',')) for _ in range(m)]
check = defaultdict(int)
for i in memo:
    check[i] = 1
for i in blog:
    for j in i:
        if j in check:
            del check[j]
    print(len(check))

# set 사용 답
n, m = map(int, input().split())
keywords = set()
for _ in range(n):
    keywords.add(input().strip())

for _ in range(m):
    posts = list(input().strip().split(","))
    for post in posts:
        keywords.discard(post)
    print(len(keywords))