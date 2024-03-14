def ct(start, end, lst, list):
    m = (end - start) // 3
    if m == 1:
        for i in range(start + m, end - m):
            list[i] = ' '
        return m
    for i in range(start + m, end - m):
        list[i] = ' '
    ct(start, start + m, lst[:start + m], list)
    ct(end - m, end, lst[end - m:], list)
while True:
    try:
        n=int(input())
        lst = list('-' * (3 ** n))
        if n == 0:
            print('-')
        else:
            ct(0,len(lst),lst,lst)
            print(*lst,sep='',)
    except:
        break

#시간줄이기
def solve(n):
    if n == 1:
        return "-"
    else:
        left = solve(n // 3)
        center = " " * (n // 3)
        return left + center + left

while True:
    try:
        N = int(input())
        rst = solve(3 ** N)
        print(rst)
    except:
        break
#left와 center만 만들고 이어붙이기