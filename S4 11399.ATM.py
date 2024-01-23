N=int(input())
people=list(map(int,input().split()))
people.sort()
answer=0
# for i in range(N-1,-1,-1):
#     for j in range(i+1):
#         answer+=people[j]
for i in range(1,N+1):
    answer+=sum(people[0:i])
print(answer)