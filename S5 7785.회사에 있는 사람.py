import sys
N=int(sys.stdin.readline())
log_lst=dict()
for i in range(N):
    name,log=sys.stdin.readline().split()
    if log == 'enter':
        log_lst[name]=True
    else:
        log_lst[name]=False

ans=sorted(log_lst.keys(),reverse=True)
for key in ans:
    if log_lst[key] == True:
        print(key)

#리스트는 시간초과
#set으로 가능
n = int(input())
people = set()

for _ in range(n):
    name, state = input().split()
    if state == 'enter':
        people.add(name)
    else:
        people.discard(name)

people_list = sorted(people, reverse=True)
print('\n'.join(people_list))