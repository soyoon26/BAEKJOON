score=input()
a_score=0
b_score=0
a_win=0
b_win=0
for i in score:
    if i == 'A':
        a_score+=1
        if a_score==21:
            a_win+=1
            print(f'{a_score}-{b_score}')
            a_score,b_score = 0,0
    else:
        b_score+=1
        if b_score==21:
            b_win+=1
            print(f'{a_score}-{b_score}')
            a_score,b_score= 0,0
if a_win>b_win:
    print('A')
else:
    print('B')

