import sys
n = int(sys.stdin.readline().rstrip())
nums = list(int(sys.stdin.readline().rstrip()) for _ in range(n))

avg = round(sum(nums)/n)
print(avg)

nums.sort()
mid = nums[n//2]
print(mid)

n_dict=dict()
for i in nums:
    if i not in n_dict:
        n_dict[i] = 1
    else:
        n_dict[i] += 1
v_lst = list(n_dict.values())
maxN = max(v_lst)
n_set = set(nums)
mode = []
for i in n_set:
    if n_dict[i] == maxN:
        mode.append(i)
mode.sort()
if len(mode) > 1:
    print(mode[1])
else:
    print(mode[0])

range = max(nums)-min(nums)
print(range)

#최빈값 쉽게 구하는 법
from collections import Counter
Counter(n_set).most_common(2) #1개 원소 리스트를 넣어도 오류나지 않음, 상위 2개 구하기

#예전에도 Counter을 썼었는데 이번에는 생각이 나지 않았나보다 ㅋㅋ