N = int(input())
A=set(map(int,input().split()))
M = int(input())
M_lst=list(map(int,input().split()))

for i in M_lst:
    if i in A:
        print(1)
    else:
        print(0)

#list 시간초과로 set으로 설정