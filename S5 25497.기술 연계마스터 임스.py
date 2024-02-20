import sys
N=int(sys.stdin.readline().rstrip())
play=sys.stdin.readline().rstrip()
cnt=0
stack=[]
pre=['L','S']
for i in play:
    if i in pre:
        stack.append(i)
    elif i =='R':
        if 'L' in stack:
            cnt+=1
            stack.pop(stack.index('L'))
        else:
            break
    elif i =='K':
        if 'S' in stack:
            cnt+=1
            stack.pop(stack.index('S'))
        else:
            break
    else:
        cnt+=1
print(cnt)

#각자 cnt만들면 시간 감소
king = int(input())
skill = input()
count = 0 #사용한 기술 총 횟수
Ls, Ss = 0, 0 #사전기술 사용 횟수

for i in skill:
    if i == 'L':
        Ls += 1
    elif i == 'R':
        if Ls > 0:
            count += 1
            Ls -= 1
        else:
            break

    elif i == 'S':
        Ss += 1
    elif i == 'K':
        if Ss > 0:
            count += 1
            Ss -= 1
        else:
            break
    else:
        count += 1 #1~9기술

print(count)
