N = int(input())
lst = []
for i in range(N):
    lst += [int(input())]
lst = sorted(lst)

for i in lst:
    print(i)