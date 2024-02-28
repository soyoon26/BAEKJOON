from collections import deque
N=int(input())
lst=deque(range(1,N+1))
cnt=1
while len(lst) != 1:
    lst.rotate(-cnt**3)
    lst.pop()
    cnt+=1
print(*lst)
