#중간고사의 번호가 들어옴
import sys
N = int(input())
ans=[0]*N
final = list(map(int,sys.stdin.readline().split()))
for i in range(N):
    ans[i]=final.index(i+1)+1
    print((i+1)-ans[i])




#예시

#5
#3 2 4 1 5

#5
#1 2 3 4 5

#2 5 4 1 3
#4 1 5 3 2 원래대로 하면

#-3 1 -2 1 3
