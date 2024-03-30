import sys
n,k=map(int,sys.stdin.readline().split())
answer=[]
for i in range(1,int(n**(1/2))+1):
    if n%i==0:
        answer.append(i)
        if i**2 != n:
            answer.append(n//i)
answer.sort()

try:
    print(answer[k-1])
except:
    print(0)

#그냥 for문을 루트 사용하지말고 돌리며 len이 k가 되면 break, k보다 작으면 0 출력 아니면 print(i)출력 