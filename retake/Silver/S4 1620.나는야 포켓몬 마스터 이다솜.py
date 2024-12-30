import sys
N,M=map(int,input().split())
poke_dict={}
for i in range(N):
    poke=sys.stdin.readline().rstrip()
    poke_dict[poke]=i+1
    poke_dict[i+1]=poke
for i in range(M):
    test=sys.stdin.readline().rstrip()
    if test.isdigit():
        print(poke_dict[int(test)])
    else:
        print(poke_dict[test])
