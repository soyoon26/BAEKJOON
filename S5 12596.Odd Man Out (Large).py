N= int(input())
for n in range(1,N+1):
    G=int(input())
    lst = list(map(int,input().split()))
    set_lst=set(lst)
    for i in set_lst:
        if lst.count(i)==1:
            answer = i
    print(f'Case #{n}: {answer}')

#dict 사용
import sys
input=sys.stdin.readline;

test=int(input());

for i in range(test):
    seat=dict();
    member=int(input());

    guest=list(map(int,input().split()));

    for j in guest:
        if(j not in seat):
            seat[j]=1;
        else:
            seat[j]+=1;

    print("Case #%d: "%(i+1),end='');
    for j in seat.items():
        if(j[1]==1):
            print(j[0]);
            break;