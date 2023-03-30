T = int(input())
for tc in range(T):
    result = list(input())
    cnt = 0
    cnt_lst = []
    for i in range(len(result)):

        if result[i] == 'O':
            cnt += 1
            cnt_lst.append(cnt)
        else:
            cnt = 0
    print(sum(cnt_lst))