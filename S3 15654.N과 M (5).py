N,M=map(int,input().split())
num=list(map(int,input().split()))

num.sort()
answer = []

def back():
    if len(answer) == M:
        print(*answer)
        return
    for i in num:
        if i not in answer:
            answer.append(i)
            back()
            answer.pop()
back()

