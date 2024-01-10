M = int(input())
N = int(input())
p_lst = []
for i in range(M,N+1):
    for j in range(2,int(i**0.5)+2):
        if i%j == 0:
            break
        elif j == int(i**0.5)+1:
            if i == 1:
                pass
            else:
                p_lst.append(i)
if M <=2 and 2 <= N:
    p_lst.append(2)
p_lst.sort()
if p_lst :
    print(sum(p_lst))
    print(p_lst[0])
else :
    print(-1)

#2인 경우도 생각하기
#
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# M = int(input())
# N = int(input())
#
# prime_numbers = [num for num in range(M, N + 1) if is_prime(num)]
#
# if prime_numbers:
#     print(sum(prime_numbers))
#     print(min(prime_numbers))
# else:
#     print(-1)
