N=int(input())
people = []
for i in range(N):
    person=tuple(map(int,input().split()))
    people.append(person)
answer=[]
for j in people:
    ans=0
    for k in range(N):
        if j[0] < people[k][0] and j[1] < people[k][1]:
            ans+=1
    answer.append(ans+1)
print(*answer)
