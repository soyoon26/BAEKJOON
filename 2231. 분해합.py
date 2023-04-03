N = int(input())
sum = 0
ans = []
for i in range(1,1000001):
    sum = 0
    ii = str(i)
    for j in ii:
        sum += int(j)

    if i + sum == N:
        ans.append(i)
try :
    print(min(ans))
except :
    print(0)