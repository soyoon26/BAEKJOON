N=int(input())
num=1
for i in range(1,N+1):
    num*=i
num=list(str(num))
answer=0
for j in range(len(num)-1,-1,-1):
    if num[j] == '0':
        answer+=1
    else:
        break
print(answer)