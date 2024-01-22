N= int(input())
book=[input() for _ in range(N)]
book_set= set(book)
ans_list=[]
for i in book_set:
    j=book.count(i)
    ans_list.append([j,i])
ans_list.sort(key = lambda x:(-x[0],x[1]))
print(ans_list[0][1])

#더하는 방법으로 풀기
n=int(input())
d={}
for i in range(n):
    s=input()
    if s not in d:
        d[s]=1
    else:
        d[s]+=1
max=0
for i in d:
    if d[i]>max:
        max=d[i]
        ans=i
    elif d[i]==max and ans>i:#사전순
        ans=i