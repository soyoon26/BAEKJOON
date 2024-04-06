import sys, math
while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    cnt = 0

    def check(k):
        global cnt
        for i in range(2,int(math.sqrt(k))+1):
            if k % i == 0:
                return 0
        return 1

    for i in range(n+1,2*n+1):
        cnt += check(i)
    if n == 1:
        print(1)
    else:
        print(cnt)


# 더 빠른 방법
# 1. 미리 소수 판별 리스트를 생성
bool_list = [True] * (123456*2 + 1)
for i in range(2, int((123456*2 + 1) ** 0.5)):
    if bool_list[i]:
        for j in range(i*2, 123456*2 + 1, i):
            bool_list[j] = False

# 2. 입력값이 0이 아닐 때까지 반복
while(n:=int(input())): # 바다코끼리 연산자 : 할당과 연산을 동시에 처리
    print(len([i for i in range(n+1, 2*n+1) if bool_list[i]]))