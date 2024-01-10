# X= int(input())
# N=0
# num=0
# ans=''
# for i in range(X,0,-1):
#     if X>=(((1+i)*i)/2):
#         N=i
#         num=int(X-(((1+i)*i)/2)) #나머지
#         break
#
#
# if num == 0: #저번 것의 마지막번째
#     if N%2==0:
#         print(N,'/1',sep='')#짝수
#     else:
#         print('1/',N,sep='')
# else:
#     if N%2!=0: #홀수
#         print(num,'/',N-num+2,sep='')
#     else: #짝수
#         print(N-num+2,'/',num,sep='')
# # 시간초과
#
X=int(input())
sum=0
N=0
num=0

for i in range(1,X+1):
    sum += i
    if X <= sum:
        N=i-1
        num= X-(sum-i)
        break
if num == 0: #저번 것의 마지막번째
    if N%2==0:
        print(N,'/1',sep='')#짝수
    else:
        print('1/',N,sep='')
else:
    if N%2!=0: #홀수
        print(num,'/',N-num+2,sep='')
    else: #짝수
        print(N-num+2,'/',num,sep='')

# n = int(input())
#
# for i in range(n+1):
#     if n <= i*(i+1)/2:
#         new_n = int(n - i*(i-1)/2)
#         if i%2==0:
#             print(str(new_n)+'/'+str(i+1-new_n))
#         else:
#             print(str(i+1-new_n)+'/'+str(new_n))
#         break

# a=int(input())
# b=1
# while a>(b+1)*b/2:
#     b+=1
# if b%2==0:
#
#     print(str(int(a - ((b - 1) * b / 2))) + "/" + str(int(((b + 1) * b / 2) - a + 1)))
# else:
#     print(str(int(((b + 1) * b / 2) - a + 1)) + "/" + str(int(a - ((b - 1) * b / 2))))
#while 사용