num_lst = [int(i) for i in input()]
num_lst.sort()
for i in range(len(num_lst)-1,-1,-1):
    print(num_lst[i],end='')