N = int(input())
for i in range(1,N+1):
        print(' '*(N-i)+'* '*i)

##출력결과 끝부분
N = int(input())
for i in range(1,N):
        print(' '*(N-i)+'* '*i)
print('*'+' *'*(N-1))