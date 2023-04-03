N = int(input())
num_lst = list(map(int,input().split()))
cnt = 0
for i in num_lst:
    for j in range(2,i):
        if i % j == 0:
            cnt += 1
            break

if 1 in num_lst:
    print(len(num_lst)- cnt - 1)
else:
    print(len(num_lst) - cnt)

