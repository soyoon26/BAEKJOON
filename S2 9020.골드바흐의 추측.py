import sys, math
T = int(sys.stdin.readline().rstrip())
for t in range(T):
    n = int(sys.stdin.readline().rstrip())
    a = b= n//2
    def check(k):
        for i in range(2,int(math.sqrt(k))+1):
            if k % i == 0:
                return False
        return True
    while True:
        if check(a) and check(b):
            print(a,b)
            break
        else:
            a = a - 1
            b = b + 1
            
# 차가 작은 수를 구해야 하니까 중간부터 시작
#소수를 구해야 하니까 sqrt사용한 범위까지 나누어 떨어지면 소수가 아닌 것
