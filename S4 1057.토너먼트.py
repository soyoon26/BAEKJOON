import sys
from collections import deque
N,jimin,hansoo=map(int,sys.stdin.readline().split())
round=0
while jimin != hansoo:
    round+=1
    jimin=jimin-jimin//2
    hansoo=hansoo-hansoo//2
print(round)
