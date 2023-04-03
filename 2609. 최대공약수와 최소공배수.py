A,B = map(int,input().split())
GCD = 0
LCM = 0
for i in range(1,100000001):
    if A >= i and B >= i:
        if A % i == 0 and B % i == 0:
            GCD = i
    if i >= A and i >= B:
        if i % A == 0 and i % B == 0:
            LCM = i
            break
print(GCD)
print(LCM)