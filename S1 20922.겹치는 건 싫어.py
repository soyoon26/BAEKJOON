import sys
from collections import defaultdict
n,k = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))
dict = defaultdict(int)
answer = [] # 제일 큰 값 출력
# 딕셔너리 하나라도 k가 되면 끝.... 디폴트딕셔너리
ans, start, end=0,0,0

while end < n: #end가 끝까지 갈 때까지
    if dict[nums[end]]>=k:
        dict[nums[start]]-=1 #k와 같아지면 같은 수를 빼도록 start를 더해줌
        start +=1
    else:
        dict[nums[end]]+=1
        end+=1
        ans = max(ans,end-start) #갱신
# start가 end와 같아질때까지 1을 빼면서 앞으로
# 최장 연속 부분 수열 길이 출력
print(ans)