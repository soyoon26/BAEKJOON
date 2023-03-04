L = int(input()) #케이크 길이
N =  int(input()) #방청객 수
cake = [0]*L
# print(cake)
max_want = 0
max_want_num = 0
max_real = 0
max_real_num = 0
for i in range(1,N+1):
    P, K = map(int,input().split())
    if max_want < K-P+1:
        max_want = K-P+1
        max_want_num = i
    for j in range(P-1,K):
        if cake[j] == 0:
            cake[j] = i
    if max_real < cake.count(i):
        max_real = cake.count(i)
        max_real_num = i

print(max_want_num)
print(max_real_num)



