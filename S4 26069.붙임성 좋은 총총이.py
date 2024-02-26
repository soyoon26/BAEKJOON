import sys
n=int(sys.stdin.readline().rstrip())
dance=['ChongChong']
for i in range(n):
    A,B=sys.stdin.readline().split()
    if A in dance or B in dance:
        dance.append(A)
        dance.append(B)
print(len(set(dance)))