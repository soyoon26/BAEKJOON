T=int(input())
for t in range(T):
    N=int(input())
    num=[1,1,1,2,2]+[0]*(N-5)
    for i in range(5,N):
        num[i]=num[i-5]+num[i-1]
    print(num[N-1])