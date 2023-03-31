music = [int(i) for i in input().split()]
sum = 0
for i in range(1,9):
    one = music.index(1)
    eight = music.index(8)

    if i == music[i-1]:
        sum += 1

    elif one == eight + 1:
        for j in range(one,7):
            if music[j] + 1 == music[j+1] :
                sum -= 10
        for k in range(0,eight+1):
            if music[k] + 1 == music[k+1] :
                sum -= 10

    elif 9-i == music[i-1]:
        sum -= 1

    elif one == eight - 1:
        for j in range(eight, 7):
            if music[j] - 1 == music[j + 1]:
                sum -= 1
        for k in range(0, one + 1):
            if music[k] - 1 == music[k + 1]:
                sum -= 1
        sum -= 1

if sum == 8 or sum == -480:
    print('ascending')

elif sum == -8 or sum == -56 :
    print('descending')
else:
    print('mixed')