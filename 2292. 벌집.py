N = int(input())
for n in range(1000000000):
    if N-1 <= n*(n+1)*3:
        print(n+1)
        break