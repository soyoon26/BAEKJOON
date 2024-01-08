num = []
num_sum = 0
for i in range(5):
    num.append(int(input()))
    num_sum += num[i]
print(int(num_sum/5))
num.sort()
print(num[2])