N,M = map(int,input().split())
balls = list(range(1,N+1))
for _ in range(M):
    i,j = map(int,input().split())
    balls[i-1:j] = reversed(balls[i-1:j])

print(' '.join(map(str,balls)))
#join 사용, 문자열 가능
