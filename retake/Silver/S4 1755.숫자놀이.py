
import sys
print = sys.stdout.write

m, n = map(int, input().split())

alpha = ['ze', 'on', 'tw', 'th', 'fo', 'fi', 'si', 'se', 'ei', 'ni']
number = []
for a in range(m, n + 1):
    english = ''
    x, y = a // 10, a % 10
    if x:
        english = alpha[x]
    english += alpha[y]

    number.append((english, a))

number.sort()

for i, x in enumerate(number):
    _, v = x
    print(str(v) + ' ')
    if i % 10 == 9:
        print('\n')
