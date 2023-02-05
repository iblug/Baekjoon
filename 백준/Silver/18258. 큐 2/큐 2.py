import sys
from collections import deque
input = sys.stdin.readline

def act(q:deque, com, num):
    if com == 'push':
        q.append(num)
    if com == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    if com == 'size':
        print(len(q))
    if com == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    if com == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    if com == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)

q = deque()
for _ in range(int(input())):
    com, *num = input().rstrip().split()
    if num:
        num = int(num[0])
    act(q, com, num)