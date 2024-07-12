import sys
T = int(sys.stdin.readline().rstrip())
for t in range(T):
    n = int(sys.stdin.readline().rstrip())
    alcohol = 0
    answer = ""
    for i in range(n):

        a, l = sys.stdin.readline().split()
        if int(l) > alcohol:
            alcohol = int(l)
            answer = a
    print(answer)
