A, B= map(int,input().split())
answer= 1
while B != A:
    if B%2 == 0:
        B = B//2
        answer+=1
    elif str(B)[-1] == '1':
        B=str(B)[:-1]
        B=int(B)
        answer+=1
    else:
        answer=-1
        break
    if B < A :
        answer=-1
        break
print(answer)


# 더 간결한 방법
import sys
input = sys.stdin.readline

A, B = map(int,input().split())
cnt = 1
while B > A:
    if B % 10 == 1:
        B //= 10
    elif B % 2 == 0:
        B //= 2
    else:
        break
    cnt += 1

print(cnt if A == B else -1)