import sys
N=int(sys.stdin.readline())
nums=[]
for n in range(N):
    num=sys.stdin.readline().rstrip()
    nums.append(num)
for i in range(len(nums[0])-1,-1,-1):
    cnt=0
    for j in range(N):
        for k in range(j+1,N):
            #print(nums[j][i:],nums[k][i:])
            if nums[j][i:] == nums[k][i:]:
                break
            else:
                cnt+=1
    if cnt == ((N-1)*N)//2:
        answer=len(nums[j][i:])
        break
print(answer)

#시간 줄이기
count = int(input())
id = []

for n in range(count):
    id.append(sys.stdin.readline().strip("\n"))

index = 1
while True:
    temp = [*id]
    temp_set = set()
    if index == len(temp[0]):
        print(index)
        break
    for n in temp:
        temp_set.add(n[-1:(len(n)-index-1):-1])
    if len(temp_set) == len(id):
        print(index)
        break
    else:
        index+=1
