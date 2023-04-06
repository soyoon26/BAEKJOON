N = int(input())
str_lst = []
for i in range(N):
    i = input()
    str_lst += [(len(i),i)]
str_lst=set(str_lst)
len_lst = sorted(str_lst)

for i in range(len(len_lst)):
    print(len_lst[i][1])
