import sys
num=map(int,sys.stdin.readline().split())
min=min(num)
burger=list(map(int,sys.stdin.readline().split()))
side=list(map(int,sys.stdin.readline().split()))
beverage=list(map(int,sys.stdin.readline().split()))
burger.sort(reverse=True)
side.sort(reverse=True)
beverage.sort(reverse=True)
price=0

for i in range(min):
    price+=(burger[i]+side[i]+beverage[i])*0.9
print(sum(burger)+sum(side)+sum(beverage))
print(int(price)+sum(burger[min:])+sum(side[min:])+sum(beverage[min:]))