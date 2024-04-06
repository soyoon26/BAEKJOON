import sys
n, m = map(int,sys.stdin.readline().split())
nums = [True for _ in range(1000001)]
nums[1] = False
for i in range(2,int(1000000 ** 0.5)+1):
    for j in range(i*2,1000001,i):
        nums[j] = False

print(*list(i for i in range(n,m+1) if nums[i]),sep='\n')

#사실 while로 돌리지 않기 때문에 미리 구해놓지 않아도 되지만 앞서 본 방법이라 써봤닿 우하하


# for대신 while을 쓴 방법
# for ch in range(2, int(num**(1/2))+1):
#         tns = ch*2 제곱근보다 작으면 배수들 False처리하기
#         while tns <= num:
#             checklist[tns] = False
#             tns += ch