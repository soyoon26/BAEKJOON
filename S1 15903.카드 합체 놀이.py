import sys, heapq
n,m=map(int,sys.stdin.readline().split())
cards=list(map(int,sys.stdin.readline().split()))
cards.sort()
while m > 0:
    x = heapq.heappop(cards)
    y = heapq.heappop(cards)
    heapq.heappush(cards,x+y)
    heapq.heappush(cards,x+y)
    m-=1
print(sum(cards))