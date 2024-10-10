n = int(input())
yes, no = 0,0
for i in range(n):
    opinion = int(input())
    if opinion == 1:
        yes+=1
    else:
        no+=1
if yes > no :
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")