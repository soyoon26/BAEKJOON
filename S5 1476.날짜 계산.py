ESM = list(map(int,input().split()))
if ESM[0] == ESM[1] == ESM[2] :
    print(ESM[0])
else:
    for i in range(1000):
        if ((15*i+ESM[0])-ESM[1])%28==0 and ((15*i+ESM[0])-ESM[2])%19==0:
            print(15*i+ESM[0])
            break

#다른 방법 , 같아지면 끝나니까
# while True:
#     if E == S and S == M:
#         break
#
#     if min(E, S, M) == E:
#         E += 15
#
#     elif min(E, S, M) == S:
#         S += 28
#
#     elif min(E, S, M) == M:
#         M += 19
#
# print(E)