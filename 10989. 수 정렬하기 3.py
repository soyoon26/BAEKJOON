
import sys
N = int(sys.stdin.readline().rstrip())
cnt_lst = [0]*10001

for i in range(N):
    cnt_lst[int(sys.stdin.readline().rstrip())] += 1
for i in range(1,10001):
    if cnt_lst[i]:
        for j in range(cnt_lst[i]):
            sys.stdout.write(str(i)+'\n')









