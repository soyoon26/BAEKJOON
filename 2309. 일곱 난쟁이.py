candidate = []
for i in range(9):
    candidate.append(int(input()))

ans_lst = []
def findwhois(idx,list):
    if len(list) == 7:
        ans_lst.append(list[:])
        return

    for i in range(idx,len(candidate)):
        findwhois(i+1,list+[candidate[i]])

findwhois(0,[])
ans = []
for i in range(len(ans_lst)):
    if sum(ans_lst[i]) == 100:
        ans.append(ans_lst[i])
print(*sorted(ans[0]),sep='\n')
