import sys
eg=['ze','on','tw','th','fo','fi','si','se','ei','ni']
M,N=map(int,sys.stdin.readline().split())
lst=list(range(M,N+1))
dict=dict()
for i in range(10):
    dict[eg[i]]=i
str_n=[]
for i in lst:
    n=''
    for j in str(i):
        n+=eg[int(j)]
    str_n.append(n)
str_n.sort()
ans=[]
for j in str_n:
    answer=''
    for k in range(0,len(j),2):
        answer+=str(dict[j[k]+j[k+1]])
    ans.append(int(answer))
for m in range(0,len(ans),10):
    print(*ans[m:m+10])

#더 편한 방법
import sys
print = sys.stdout.write

m, n = map(int, input().split())

alpha = ['ze', 'on', 'tw', 'th', 'fo', 'fi', 'si', 'se', 'ei', 'ni']
number = []
for a in range(m, n + 1):
    english = ''
    x, y = a // 10, a % 10
    if x:
        english = alpha[x]
    english += alpha[y]

    number.append((english, a))

number.sort()

for i, x in enumerate(number):
    _, v = x
    print(str(v) + ' ')
    if i % 10 == 9:
        print('\n')