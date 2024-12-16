def input():return sys.stdin.readline().rstrip()

n = int(input())
lst = [0]
for i in list(map(int, input().split())):
    lst.append(lst[-1] + i)
for i in range(int(input())):
    x, y = map(int, input().split())
    print(lst[y]-lst[x-1])
