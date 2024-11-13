import sys
input = sys.stdin.readline

def zeros(n):
    count = 0
    i = 5
    while n // i > 0:
        count += n // i
        i *= 5
    return count

def find(m):
    left, right = 0, 5 * m
    answer = -1
    while left <= right:
        mid = (left + right) // 2
        zero_count = zeros(mid)
        if zero_count == m:
            answer = mid
            right = mid - 1
        elif zero_count < m:
            left = mid + 1
        else:
            right = mid - 1

    return answer

m = int(input().rstrip())
result = find(m)
print(result)
