N, M = map(int,input().split())
basket = [n for n in range(1,N+1)]
#basket = list(range(1,N+1))
empty = 0
for m in range(M):
    i,j = map(int,input().split())
    #i번 바구니와 j번 바구니 공 교환
    empty = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1]=empty
print(*basket)