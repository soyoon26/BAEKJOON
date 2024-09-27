import sys
n = int(sys.stdin.readline())
students = list(map(int,sys.stdin.readline().split()))
other = list()
snack = list()
for i in students:
    if snack:
        while other and snack[-1]+1 == other[-1]:
            snack.append(other.pop())
        if i == snack[-1] +1:
            snack.append(i)
        else:
            other.append(i)
    else:
        if i == 1:
            snack.append(i)
        else:
            other.append(i)

for i in other[-1::-1]:
    if snack[-1]+1 == i:
        snack.append(other.pop())
    else:
        print("Sad")
        break
if len(snack) == n:
    print("Nice")
