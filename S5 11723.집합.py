import sys
M= int(sys.stdin.readline().strip())
S=set()
for m in range(M):
    c = sys.stdin.readline().strip()
    # print(c)
    # print(c[0],'뭐임')
    # print(c[-2:],'뭐지')
    if c[:3] == 'add':
        S.add(c[-2:])
    elif c[:6] == 'remove':
        S.discard(c[-2:])
        # print(S)
    elif c[:5] == 'check':
        if c[-2:] in S:
            print('1')
        else:
            print('0')
    elif c[:6] == 'toggle':
        if c[-2:] in S:
            S.discard(c[-2:])
        else:
            S.add(c[-2:])
        # print(S)
    elif c == 'all':
        S={' 1',' 2,'' 3',' 4',' 5',' 6',' 7',' 8',' 9','10','11','12','13','14','15','16','17','18','19','20'}
    else:
        S=set()

#다른 방법

import sys

M = int(input())
lst = []
for i in range(M):
    a = sys.stdin.readline().split()
    if a[0] == 'add':
        if int(a[1]) not in lst:
            lst.append(int(a[1]))

    elif a[0] == 'remove':
        if int(a[1]) in lst:
            lst.remove(int(a[1]))
    elif a[0] == 'check':
        if int(a[1]) in lst:
            print(1)
        else:print(0)
    elif a[0] == 'toggle':
        if int(a[1]) not in lst:
            lst.append(int(a[1]))
        else:
            lst.remove(int(a[1]))
    elif a[0] == 'all':
        lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    else:
        lst = []

#리스트로 받고 if를 써서 remove 사용

