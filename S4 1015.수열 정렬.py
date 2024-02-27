import sys
N=int(sys.stdin.readline().rstrip())
A=list(map(int,sys.stdin.readline().split()))
sorted_A=sorted(A)
dict=dict()
for i in range(N):
    dict[i]=sorted_A[i]
answer=[]
for j in A:
    for key,value in dict.items():
        if j==value:
            answer.append(key)
            dict[key]=1001
            break
print(' '.join(map(str,answer)))

