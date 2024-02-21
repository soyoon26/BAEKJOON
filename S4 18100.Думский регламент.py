import sys
N=int(sys.stdin.readline().rstrip())
stack=[]
answer='Yes'
for i in range(N):
    order=sys.stdin.readline().split()
    if order[0]=='Add':
        stack.append(order[1])
    elif order[0]=='Vote' and stack:
        if stack.pop()==order[1]:
            continue
        else:
            answer='No'
            break
    elif order[0]=='Vote' and not stack:
            answer='No'
            break
if stack:
    answer='No'
print(answer)