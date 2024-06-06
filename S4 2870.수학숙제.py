import sys
n = int(sys.stdin.readline().rstrip())
nums=[]
for _ in range(n):
    word = list(sys.stdin.readline().rstrip())
    num=''
    for i in word:
        if i.isdigit():
            num+=i
        else:
            if len(num) > 0:
                nums.append(int(num))
                num = ''
    if len(num) > 0:
        nums.append(int(num))
nums.sort()
print(*nums,sep='\n')