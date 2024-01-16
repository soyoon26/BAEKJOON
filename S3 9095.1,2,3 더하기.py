T= int(input())
s=[1,2,4]+[0]*7

for i in range(3,10):
    s[i]=s[i-1]+s[i-2]+s[i-3]
for t in range(T):
    n=int(input())
    print(s[n-1])
