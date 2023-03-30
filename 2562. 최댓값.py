num_lst = []
for i in range(1,10):
    num = int(input())
    num_lst.append([num,i])

num_lst.sort(reverse = True)

print(num_lst[0][0])
print(num_lst[0][1])
