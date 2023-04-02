import sys
input = sys.stdin.readline
str = [i.upper() for i in input()]

str_lst = set(str)
sum = 0
candidate= []
for i in str_lst:
    if str.count(i) > sum:
        sum = str.count(i)
for i in str_lst:
    if str.count(i) == sum:
        candidate.append(i)
candidate= set(candidate)

if len(str) == 2:
    print(*str)
elif len(candidate) == 1:
    print(*candidate)
else:
    print("?")
