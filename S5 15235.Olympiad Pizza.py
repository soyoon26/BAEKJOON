from collections import deque

def pizza(pizzas):
    n = len(pizzas)
    times = [0] * n
    queue = deque((i, pizzas[i]) for i in range(n))
    time = 0
    while queue:
        time += 1
        idx, remaining_pizza = queue.popleft()
        remaining_pizza -= 1
        if remaining_pizza == 0:
            times[idx] = time
        else:
            queue.append((idx, remaining_pizza))
    return times

n = int(input())
pizzas = list(map(int, input().split()))

print(*pizza(pizzas))
