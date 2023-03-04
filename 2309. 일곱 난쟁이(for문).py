lst = []

for i in range(9):
    lst.append(int(input()))
flag = 0
sum_not = sum(lst) - 100
for i in range(8):
    for j in range(i+1,9):
        if lst[i] + lst[j] == sum_not:
            lst.remove(lst[i])
            lst.remove(lst[j-1])
            flag = 1
            break
    if flag == 1:
        break

lst = sorted(lst)
print(*lst,sep='\n')