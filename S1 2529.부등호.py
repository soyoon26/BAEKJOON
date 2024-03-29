import sys
N = int(sys.stdin.readline().rstrip())
lst= list(sys.stdin.readline().split())
num=[1,2,3,4,5,6,7,8,9,0]
answer=[]
answer_candi=[]
def comp(answer,lst):
    global answer_candi
    cnt=0
    for i in range(len(lst)):
        if lst[i] == '<':
            if answer[i] < answer[i+1]:
                cnt+=1
            else:
                break
        elif lst[i] == '>':
            if answer[i] > answer[i+1]:
                cnt+=1
            else:
                break
    if cnt == len(lst):
        answer_candi.append(answer[:])
        return answer_candi

def back():
    global answer_candi
    if len(answer) == len(lst)+1:
        comp(answer,lst)
        return
    for i in num:
        if i not in answer:
            answer.append(i)
            back()
            answer.pop()
back()
print(*max(answer_candi),sep='')
print(*min(answer_candi),sep='')


#빠른 방법

minN="9999999999" #문자열
maxN="0"
visited=[False]*10
def check(i,j,k):
  if(k=="<"):
    if(i<j):
      return i<j
  else:
    if(i>j):
      return i>j #맞으면 true, 틀리면 false를 return함
def dfs(signIndex,currentN):   #currentN은 답이 모이고 있음
  global maxN,minN,visited
  if(signIndex==k):
    maxN=max(maxN,currentN)
    minN=min(minN,currentN)
    return
  for i in range(0,10):
    if(visited[i]==False):
      if(check(currentN[-1],str(i),signs[signIndex])):
         visited[i]=True
         dfs(signIndex+1,currentN+str(i))
         visited[i]=False
for i in range(0,10):
    visited[i]=True
    dfs(0,str(i))
    visited=[False]*10
print(maxN)
print(minN)