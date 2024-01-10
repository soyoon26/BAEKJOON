N = int(input())
sg = set(map(int,input().split()))
M = int(input())
num = list(map(int,input().split()))
for i in range(M):
    if num[i] in sg:
        num[i] = 1
    else:
        num[i] = 0
print(*num)

#시간 확인하며 풀기
# 중복, 순서 필요없을 경우 set이 더 빠름