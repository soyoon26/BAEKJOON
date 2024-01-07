N=int(input())
answer = -1
for i in range(int(N//5),-1,-1):
    for j in range(0,(N//3)+1):
        if i*5+3*j ==N:
            answer=i+j
            break
    if answer != -1:
        break


print(answer)
#while으로 다시 풀어보기