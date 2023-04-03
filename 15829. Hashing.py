r = 31
M = 1234567891
L = int(input())
str= input()
str_sum = 0
s= []
for i in range(L):
    str_sum += ((ord(str[i])-96)*(r**i))

print(str_sum%M)
