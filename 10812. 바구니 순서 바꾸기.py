N,M = map(int,input().split())
num_lst = []
for i in range(1,N+1):
    num_lst.append(i)
for m in range(M):
    numbers = []
    i,j,k = map(int,input().split())
    for l in range(j-i+1):
        numbers.append(num_lst.pop(i-1))
    for x in range(k-i):
        numbers.append(numbers.pop(0))
    for y in range(j-i+1):
        num_lst.insert(i+y-1,numbers[y])
print(*num_lst,sep=" ")


