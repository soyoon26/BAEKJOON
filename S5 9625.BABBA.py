import sys
K=int(sys.stdin.readline().rstrip())
a=[1]+[0]*45
b=[0]+[0]*45
for i in range(1,K+1):
    a[i]=b[i-1]
    b[i]=a[i-1]+b[i-1]

print(a[K],b[K])

#시간 줄이기
K = int(input())
cnts = [0, 1]
for i in range(K-1):
    cnts.append(cnts[-1]+cnts[-2])
print(cnts[-2], cnts[-1])