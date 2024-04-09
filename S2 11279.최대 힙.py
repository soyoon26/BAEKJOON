import heapq, sys
N = int(sys.stdin.readline().rstrip())
heap=[]
heapq.heapify(heap)

for i in range(N):
    x = int(sys.stdin.readline().rstrip())
    if x > 0:
        heapq.heappush(heap,-x)
    else:
        if heap:
            max = -heapq.heappop(heap)
            print(max)
        else:
            print(0)