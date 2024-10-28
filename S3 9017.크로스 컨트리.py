import sys
from collections import defaultdict
T = int(sys.stdin.readline().rstrip())
for t in range(T):
    ranking = defaultdict(list)
    n = int(sys.stdin.readline().rstrip())
    runners = list(map(int,sys.stdin.readline().split()))
    check = set(runners)
    team = list()
    for c in check:
        if runners.count(c) >= 6:
            team.append(c)
    cnt=1
    for i in range(n):
        if runners[i] in team:
            ranking[runners[i]].append(cnt)
            cnt += 1
    answer=[float('inf'),float('inf'),float('inf')]
    for key,value in ranking.items():
        if len(value) >= 6:
            if answer[0] > sum(value[:4]):
                answer[0] = sum(value[:4])
                answer[1] = value[4]
                answer[2] = int(key)
            elif answer[0] == sum(value[:4]):
                if answer[1] > value[4]:
                    answer[0] = sum(value[:4])
                    answer[1] = value[4]
                    answer[2] = int(key)

    print(answer[2])

