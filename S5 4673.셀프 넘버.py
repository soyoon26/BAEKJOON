lst= [i for i in range(1,10000)]
new_lst=[]

for i in range(1,10000):
    if i + sum(int(j) for j in str(i)) < 10000:
        new_lst.append(i + sum(int(j) for j in str(i)))

answer=[]
for k in lst:
    if k not in new_lst:
        answer.append(k)
for i in answer:
    print(i)


#시간 빠른 방법
def d(n):
    output = n
    for c in str(n):
        output += int(c)
    return output

dn2n = {}
for i in range(1, 10000):
    dn2n[d(i)] = i
    if i not in dn2n:
        print(i)

#set이용,빼기 적용
def d(n):
    return n + sum(map(int, str(n)))
def self_numbers(limit):
    numbers = set(range(limit))
    not_self_numbers = set()
    for i in range(limit):
        self_number = d(i)
        if self_number < limit:
            not_self_numbers.add(self_number)
    return sorted(numbers - not_self_numbers)

result = self_numbers(10001)
print(*result, sep = '\n')