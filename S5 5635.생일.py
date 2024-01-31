N = int(input())
lst=[]
for i in range(N):
    data = input().split()
    data[1:]=map(int,data[1:])
    lst.append(data)
lst.sort(key=lambda x:(x[3],x[2],x[1]))
print(lst[-1][0],lst[0][0],sep='\n')