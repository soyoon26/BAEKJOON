import sys
A,B=map(int,sys.stdin.readline().split())
a=set(map(int,sys.stdin.readline().split()))
b=set(map(int,sys.stdin.readline().split()))
answer=0
ans_a=a-b
ans_b=b-a
print(len(ans_a)+len(ans_b))

#대칭차집합
#A.symmetric_difference(B)
#A^B