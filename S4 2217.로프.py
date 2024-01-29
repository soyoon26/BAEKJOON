N=int(input())
lst = []
new_lst=[]
for i in range(N):
    lst.append(int(input()))
lst.sort()
for j in range(N):
    new_lst.append((N-j)*lst[j])
print(max(new_lst))

#for문 말고 받는 방법
#r=[int(sys.stdin.readline()) for _ in range(n)]