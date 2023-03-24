a, b, c = map(int,input().split())
max_num = max(a,b,c)
num_lst = [a,b,c]
if a == b == c:
    print(10000 + a*1000)
elif a != b and b != c and a != c :
    print(max_num*100)
for i in num_lst:
    if num_lst.count(i) == 2:
        print(1000+i*100)
        break


