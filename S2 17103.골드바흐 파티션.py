import sys
T = int(sys.stdin.readline().rstrip())
prime = [1]*1000001
for i in range(2,1000001):
    for j in range(i*2,1000001,i):
        prime[j] = 0
for t in range(T):
    n = int(sys.stdin.readline().rstrip())
    answer = 0
    for i in range(2,n//2+1):
        if prime[i] + prime[n-i] == 2:
            answer += 1
    print(answer)