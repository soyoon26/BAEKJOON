N=input()
num=int(N,8) #8진수를 10진수로 바꾸기
ans=bin(num) #10진수를 2진수로 바꾸기
print(ans[2:])

#시간초과
# num=[]
# ans=[]
# for i in range(len(N)):
#     num.append(int(N[i])*8**(int(len(N))-i-1))
# num=sum(num)
# while num != 0:
#     ans.append(str(num%2))
#     num=num//2
# print(*ans[::-1],sep='')
#reversed_str = ''.join(reversed(my_str))