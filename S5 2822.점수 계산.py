score = [[int(input()),_+1] for _ in range(8)]
score.sort(reverse=True)
total = score[:5]
answer = sorted(total,key=lambda x:x[1])
total_sum = sum(item[0] for item in total)
print(total_sum)
print(*list(item[1] for item in answer))
