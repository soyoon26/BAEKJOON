A=input()
B=input()
num=''

for i in range(8):
    num+=A[i]+B[i] #A.insert(i,B)
while len(num) != 2:
    lst=[] #lst.clear()
    for i in range(0,len(num)-1):
        lst.append((int(num[i])+int(num[i+1]))%10)
    num=lst
print(*num,sep='')