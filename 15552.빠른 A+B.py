import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    A, B= map(int,sys.stdin.readline().rstrip().split())
    #개행문자 제거
    print(A+B)
