import sys
an,bn=map(int,sys.stdin.readline().split())
A=set(map(int,sys.stdin.readline().split()))
B=set(map(int,sys.stdin.readline().split()))
ans=list(A-B)
ans.sort()
print(len(ans))
print(*ans)

#시간줄이기
#for b in B:
#    if b in element_dict:
#        del element_dict[b]