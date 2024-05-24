import sys
from collections import defaultdict
n= int(sys.stdin.readline().rstrip())
nums=list(map(int,sys.stdin.readline().split()))
symbols = list(map(int,sys.stdin.readline().split()))
symbol=defaultdict(int)
for i in range(4):
    if i == 0:
        symbol['+']=symbols[i]
    elif i == 1:
        symbol['-']=symbols[i]
    elif i == 2:
        symbol['*']=symbols[i]
    else:
        symbol['/']=symbols[i]
s=['+','-','*','/']
ans=[]
min=10**9
max=-10**9
def math():
    global min
    global max
    answer=nums[0]
    for i in range(n-1):
        if ans[i] == '+':
            answer+=nums[i+1]
        elif ans[i] == '-':
            answer-=nums[i+1]
        elif ans[i] == '*':
            answer*=nums[i+1]
        else:
            if answer < 0:
                answer=-answer
                answer//=nums[i+1]
                answer=-answer
            else:
                answer//=nums[i+1]
    if min > answer:
        min = answer
    if max < answer:
        max = answer
def back():
    if len(ans) == n-1:
        math()
        return
    for i in s:
        if symbol[i] > 0:
            symbol[i] -= 1
            ans.append(i)
            back()
            symbol[i] += 1
            ans.pop()

back()
print(max)
print(min)