C= int(input())
for tc in range(C):
    score = list(map(int,input().split()))
    N= score.pop(0)
    average = int(sum(score)/N)
    cnt = 0
    for i in score:
        if i > average:
            cnt+=1

    ans = '{:.3f}'.format(round((cnt/N)*100,3))
    print(f"{ans}%")