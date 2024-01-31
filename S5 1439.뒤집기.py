S= input()
answer=0
for i in range(1,len(S)):
    if S[i] != S[0] and S[i] != S[i-1]:
        answer+=1
print(answer)