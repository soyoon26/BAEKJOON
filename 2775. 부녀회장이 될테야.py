T = int(input())
for tc in range(T):
    k = int(input()) #층
    n = int(input()) #호수
    apartment = [[0 for i in range(n)] for _ in range(k+1)]

    for j in range(0,n):
        apartment[0][j] = j+1
    for i in range(1,k+1):
        for j in range(0,n):
            for l in range(0,j+1):
                apartment[i][j] += apartment[i-1][l]

    print(apartment[k][n-1])
