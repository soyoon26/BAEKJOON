N=int(input())
for i in range(N):
    ans = 'are anagrams.'
    A,B=input().split()
    set_a=set(A)
    for j in set_a:
        if B.count(j) != A.count(j):
            ans='are NOT anagrams.'
            break
    print(A,'&',B,ans)
    
#다른 방법 : list로 만들어서 정렬시키기