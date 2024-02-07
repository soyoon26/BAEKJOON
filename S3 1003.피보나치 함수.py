N=int(input())
zero_lst=[1]+[0]*40
one_lst=[0]+[0]*40

for i in range(1,41):
    zero_lst[i]=one_lst[i-1]
    one_lst[i]=zero_lst[i-1]+one_lst[i-1]

for j in range(N):
    n=int(input())
    print(zero_lst[n],one_lst[n])