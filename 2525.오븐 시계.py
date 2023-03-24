A, B = map(int,input().split())
C= int(input())

if B+C >= 60:
    #60분이 넘어가면
    hours = (B+C)//60
    if A+hours <24:
        print(A+hours,(B+C)%60)
    else :
        print((A+hours)%24,(B+C)%60)
else: #60분이 넘어가지 않으면
    print(A,B+C)
