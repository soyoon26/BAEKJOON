import sys
str = list(sys.stdin.readline().rstrip())
str.sort()

dict = dict()
set_str=set(str)
answer=''

for i in str:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

keep=[]
for i in set_str:
    if dict[i]%2 == 0:
        answer+=i*(dict[i]//2)
    else:
        answer+=i*(dict[i]//2)
        keep.append(i)
answer=list(answer)
answer.sort()
if len(keep) < 2:
    if keep:
        print(*answer,*keep,*answer[-1::-1],sep='')
    else:
        print(*answer,*answer[-1::-1],sep='')
else:
    print("I'm Sorry Hansoo")

#다른 방법
# set을 따로 만들지 않고 처음부터 dict로만 변환해도 되었다.
# 그리고 문자열을 만든 뒤 검사하지 말고 먼저 검사하고 문자열로 변환하면 더 빠르다.

num = input()
num_dict = {}
for n in num:
    if n in num_dict:
        num_dict[n] += 1
    else:
        num_dict[n] = 1
odd = 0
odd_num = ''
for key, value in sorted(num_dict.items()):
    if value % 2 == 1:
        odd += 1
        odd_num = key
if odd > 1:
    print("I'm Sorry Hansoo")
else:
    half = ''
    for key, value in sorted(num_dict.items()):
        half += key*(value//2)
    if odd == 1:
        print(half+odd_num+half[::-1])
    else:
        print(half+half[::-1])