import sys
input = sys.stdin.readline

trie = {}

def insert(word):
    current = trie
    for char in word:
        if char not in current:
            current[char] = {}
        current = current[char]

    current['*'] = True


def check(prefix):
    current = trie
    for char in prefix:
        if char not in current:
            return False
        current = current[char]
    return True

n, m = map(int, input().split())
strings = [input().strip() for _ in range(n)]

for string in strings:
    insert(string)
answer = 0
for _ in range(m):
    word = input().strip()
    if check(word):
        answer += 1

print(answer)
