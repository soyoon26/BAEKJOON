A,B= input().split()
ans=50
for i in range(len(B)-len(A)+1):
    cnt=0
    for j in range(len(A)):
        if B[i+j] != A[j]:
            cnt+=1
    if cnt < ans:
        ans=cnt
print(ans)