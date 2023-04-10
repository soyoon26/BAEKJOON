import sys
N = int(sys.stdin.readline())

stack = []
def solve(txt):
    if len(txt) >= 6:
        stack.append(txt[5:])

    if txt == 'pop':
        if stack :
            print(stack.pop(-1))
        else:
            print(-1)

    elif txt == 'size':
        print(len(stack))

    elif txt == 'empty':
        if stack :
            print(0)
        else:
            print(1)

    elif txt == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)

for i in range(N):
    txt = sys.stdin.readline().rstrip()
    solve(txt)
