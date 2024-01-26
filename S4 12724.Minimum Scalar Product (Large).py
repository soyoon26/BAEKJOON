
T= int(input())
for t in range(1,T+1):
    n = int(input())
    x = [int(x) for x in input().split()]
    y = [int(y) for y in input().split()]

    sorted_x = sorted(x)
    sorted_y = sorted(y, reverse=True)

    answer = sum(a * b for a, b in zip(sorted_x, sorted_y))


    print(f"Case #{t}: {answer}")