N=int(input())
for n in range(N):
    num=list(map(int,input().split()))[1:]
    def gcd(a,b):
        while b != 0:
            a,b=b,a%b
        return a
    ans=[]
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            ans.append(gcd(num[i],num[j]))
    print(sum(ans))

#input()받는 방법
#n, *nums = map(int, sys.stdin.readline().split())