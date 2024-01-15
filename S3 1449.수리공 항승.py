N, L = map(int,input().split())
leak = list(map(int,input().split()))
leak.sort()
tape=1
l=0
for i in range(1,len(leak)):
    l+=leak[i]-leak[i-1]
    if l<L:
        continue
    else:
        l=0
        tape+=1
print(tape)
#
answer = 1
data.sort()
start = data[0]
for i in data[1:]:
    if i in range(start, start + L):  # 테이프 길이 안에 있다면
        continue
    else:
        start = i
        answer += 1
print(answer)

#4 5
#1 4 5 9
#답은 2

#5 2
#1 2 3 4 5
#답은 3

#5 3
#1 2 3 4 1000
#답은 3