N = int(input())
answer=0
n=0
if len(str(N))==1:
    answer=N
else:
    for i in range(1,len(str(N))):
        answer+=int('9'+(i-1)*'0')*i
    n=N-int('1'+(len(str(N))-1)*'0')+1
    answer+=9+len(str(N))*n
print(answer)
#9,90,900 개씩 더해진다.

