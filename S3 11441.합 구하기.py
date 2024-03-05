import sys
N=int(sys.stdin.readline().rstrip())
A=list(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline().rstrip())
sum=[0]*(len(A)+1)
sum[0]=A[0]
for i in range(1,len(A)):
    sum[i]=sum[i-1]+A[i]
for m in range(M):
    i,j =map(int,sys.stdin.readline().split())
    print(sum[j-1]-sum[i-2])


#다른 방법
def input():return sys.stdin.readline().rstrip()

n = int(input())
lst = [0]
for i in list(map(int, input().split())):
    lst.append(lst[-1] + i)
for i in range(int(input())):
    x, y = map(int, input().split())
    print(lst[y]-lst[x-1])