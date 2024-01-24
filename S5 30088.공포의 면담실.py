N=int(input())
time=[]

for i in range(N):
    lst=[]
    lst+=map(int,input().split())
    time.append(sum(lst[1:]))
time.sort()
time_sum=[]
for j in range(len(time)):
    time_sum.append(sum(time[:j+1]))
print(sum(time_sum))

# 더 간편한 방법
n = int(input())
data = []
result = 0

for _ in range(n):
  _, *t = list(map(int, input().split()))
  data.append(sum(t))

data.sort()

for i in range(n):
  result += data[i] * (n - i)

print(result)