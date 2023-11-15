# mem_list=list(range(1,31))
# [:]는 슬라이싱 연산이기 때문에 range를 사용해야 한다.
# range(1,31) 해야 1부터 30까지 리스트가 됨

# for _ in range(28):
#     new = int(input())
#     if new in mem_list :
#         mem_list.remove(new)
# mem_list.sort()
# for ans in mem_list:
#     print(ans)

list = [0]*30

for i in range(0,28):
    x = int(input())
    list[x-1] = 1

for j in range(30):
    if list[j] != 1:
        print(j+1)

# 처음부터 시작되니까 sort를 따로 안 써도 된다.