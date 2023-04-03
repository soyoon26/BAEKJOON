T = int(input())
for t in range(T):
    H, W, N = map(int,input().split())
    hotel = []
    for j in range(1,W+1):
        for i in range(1,H+1):
            if j < 10:
                hotel += [str(i)+'0'+str(j)]
            else:
                hotel += [str(i) + str(j)]
    print(hotel[N-1])