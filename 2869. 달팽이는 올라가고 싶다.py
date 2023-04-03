A, B, V = map(int,input().split())
cnt = 0
V=V-A
if V%(A-B):
    ans = (V//(A-B))+1
else:
    ans = V//(A-B)
print(ans+1)