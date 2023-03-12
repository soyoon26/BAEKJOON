N, X = map(int,input().split())
num_lst = [int(i) for i in input().split()]
ans = []
for num in num_lst:
    if num < X:
        ans += [num]
print(*ans,sep =' ')