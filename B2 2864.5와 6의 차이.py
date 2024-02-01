A,B=input().split()
five=[]
six=[]
for i in range(len(A)):
    if A[i] == '5':
       five.append(len(A)-i-1)
    elif A[i] == '6':
        six.append(len(A)-i-1)
for j in range(len(B)):
    if B[j] == '5':
        five.append(len(B)-j-1)
    elif B[j] == '6':
        six.append(len(B)-j-1)
ans=int(A)+int(B)
min,max=0,0
if len(five) > 0:
    for k in range(len(five)):
        max+=10**(five[k])
if len(six) > 0:
    for m in range(len(six)):
        min+=10**(six[m])
print(ans-min,ans+max)


#빠른 방법, replace 사용
a,b=input().split()
print(int(a.replace('6','5'))+int(b.replace('6','5')), end=' ')
print(int(a.replace('5','6'))+int(b.replace('5','6')))