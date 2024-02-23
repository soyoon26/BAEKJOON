import sys
from collections import deque
Alpha={'A':3,'B':2,'C':1,'D':2,'E':3,'F':3,'G':2,'H':3,'I':3,'J':2,'K':2,'L':1,'M':2,'N':2,'O':1,'P':2,'Q':2,'R':2,'S':1,'T':2,'U':1,'V':1,'W':1,'X':2,'Y':2,'Z':1}
A=sys.stdin.readline().rstrip()
B=sys.stdin.readline().rstrip()
stack=deque()

for i in range(len(A)):
    stack.append(Alpha[A[i]])
    stack.append(Alpha[B[i]])
stack_e=[]
while len(stack) != 2:
    for j in range(len(stack)-1):
        stack.append(stack[0]+stack[1])
        stack.popleft()
    stack.popleft()
print(stack[0]%10,stack[1]%10,sep='')

#chr(i+65)가 알바펫순