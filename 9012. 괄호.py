T = int(input())
for tc in range(T):
    str= input()
    sum = 0
    for i in str:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum == -1:
            break
    if sum == 0 :
        print("YES")
    else :
        print("NO")