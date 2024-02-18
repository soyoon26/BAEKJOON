from collections import Counter
import sys
N=int(sys.stdin.readline().rstrip())
nums=[]
for i in range(N):
    num=int(sys.stdin.readline().rstrip())
    nums.append(num)
nums.sort()
print(round(sum(nums)/N))
print(nums[N//2])
if N>1:
    count_num=Counter(nums).most_common(2)
    if count_num[0][1] == count_num[1][1]:
        print(count_num[1][0])
    else:
        print(count_num[0][0])
else:
    print(*nums)

print(nums[-1]-nums[0])

#Counter 사용하지 않는다면 dict사용, for문 돌려서 value값으로 key값 찾기