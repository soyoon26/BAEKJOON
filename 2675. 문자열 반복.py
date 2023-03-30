T = int(input())
for tc in range(T):
    N, str = input().split()
    str = list(str)
    N = int(N)

    for i in str:
        print(i*N,end='')
    print()