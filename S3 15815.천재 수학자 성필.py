import sys
line=list(sys.stdin.readline())
num=[]

for i in line:
    if i.isdigit():
        num.append(i)
    elif i =='+':
        ans=int(num.pop())+int(num.pop())
        num.append(ans)
    elif i =='-':
        ans=-int(num.pop())+int(num.pop())
        num.append(ans)
    elif i =='*':
        ans=int(num.pop())*int(num.pop())
        num.append(ans)
    elif i =='/':
        ans=1/int(num.pop())*int(num.pop())
        num.append(int(ans))
print(*num)


#123*+4+
#11

#pop한 건 int하지 않아도 되는 듯 + a,b로 정의해서 b//a하면 간단하다