N, M = map(int,input().split()) #카드 개수, 외치는 숫자
card_lst = list(map(int,input().split()))
ans = []
def blackjack(idx,lst):  #처음값0, n = 조합원소개수
    if len(lst) == 3:
        ans.append(lst[:])
        return
    for i in range(idx,N):
        blackjack(i+1,lst+[card_lst[i]])
blackjack(0,[])
max = 0

for i in range(len(ans)):
    if sum(ans[i]) <= M:
        if max < sum(ans[i]) :
            max = sum(ans[i])

print(max)