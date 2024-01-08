T= int(input())
prices = [int(input()) for i in range(T)]
# Q = 25, D = 10, N = 5, P = 1
for i in prices:
    Q=i//25
    q=i%25
    if q :
        D=q//10
        d=q%10
        if d:
            N=d//5
            n=d%5
            print(Q,D,N,n)
        else:
            print(Q,D,0,0)
    else: print(Q,0,0,0)
#for문 돌려서 prices다시 정의하기