N,M = map(int,input().split())
basket = [0]*N
# 바구니 갯수만큼 일단 0으로 넣어주기
for m in range(M):
    #m번 공을 넣음
    i,j,k = map(int,input().split())
    for b in range(i-1,j):
        basket[b]= k
ans = ' '.join(map(str,basket))
print(ans)

