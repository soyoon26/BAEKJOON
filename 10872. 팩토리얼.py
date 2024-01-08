N = int(input())
answer = 1
if N != 0:
    for i in range(1,N+1):
        answer *= i
print(answer)