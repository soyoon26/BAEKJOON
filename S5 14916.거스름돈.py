n = int(input())
change = [5,2]
answer = 0
if n < 5:
    if n%2:
        answer = -1
    else:
        answer = n//2
else:
    if (n%5)%2: # 하나 작게 해야 함
        answer += n//5-1
    else:
        answer += n//5
    n=n-answer*5
    answer+=n//2
print(answer)