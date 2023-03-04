N, M = map(int,input().split()) #카드 개수, 최대한 가까울 수
num_list = list(map(int,input().split()))
max = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if max < num_list[i] + num_list[j] + num_list[k] <= M:
                max = num_list[i] + num_list[j] + num_list[k]
print(max)


