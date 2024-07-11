import sys
a, b = sys.stdin.readline().split()
nums = []

def change(num,cnum,x):
    ans = ""
    for i in x:
        if i == num:
            ans+= cnum
        else:
            ans+=i
    nums.append(int(ans))

change("5","6",a)
change("6","5",a)
renums = nums.copy()
renums.sort()
nums=[]
change("5","6",b)
change("6","5",b)
nums.sort()

print(renums[0]+nums[0],renums[-1]+nums[-1])

# 며칠 안 풀었다고 replace를 까먹고 있었음..
A, B = input().split()

min_num = int(A.replace('6', '5')) + int(B.replace('6', '5'))
max_num = int(A.replace('5', '6')) + int(B.replace('5', '6'))
print(min_num, max_num)
