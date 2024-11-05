import sys, bisect
input = sys.stdin.readline
T = int(input())


def eratosthenes(n):
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p] == True:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    primes = []
    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)
    return primes
check = eratosthenes(1299709)
for t in range(T):
    k = int(input())
    if k in check:
        print(0)
    else:
        idx = bisect.bisect_left(check,k)
        if  0 < idx < len(check):
            left_prime = check[idx-1]
            right_prime = check[idx]
            print(right_prime-left_prime)
        else:
            print(0)


