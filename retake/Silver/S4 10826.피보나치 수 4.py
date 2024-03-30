n = int(input())
fb = [0]*10001
fb[0],fb[1] = 0,1
for i in range(2,n+1):
    fb[i] = fb[i-1]+fb[i-2]
print(fb[n])

#10001의 리스트를 미리 만들지 않고 append를 썼던 게 더 시간이 빠르게 걸린다.