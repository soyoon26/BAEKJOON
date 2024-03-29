N = int(input())
num5 = N//5
answer = -1
for i in range(num5,-1,-1):
    if (N-i*5)%3 == 0:
        answer=(N-i*5)//3 + i
        break
print(answer)


#저번에는 5의 for문 안에 3의 for문을 넣었는데 이제는 그럴 필요가 없는 것이 눈에 보인다.