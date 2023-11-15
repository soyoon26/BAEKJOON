A = int(input())
B = input()
# print(A*int(B[2]))
# print(A*int(B[1]))
# print(A*int(B[0]))
# print(A*int(B))

for num in B[::-1]:
    print(int(num)*A)
print(A*int(B))