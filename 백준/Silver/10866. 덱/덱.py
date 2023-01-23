import sys
input = sys.stdin.readline
from collections import deque
q = deque()
n = int(input())
for _ in range(n):
    command, *num = input().split()
    if command == 'push_front':
        q.appendleft(int(num[0]))
    if command == 'push_back':
        q.append(int(num[0]))
    if command == 'pop_front':
        if q:
            print(q.popleft())
        else:
            print(-1)
    if command == 'pop_back':
        if q:
            print(q.pop())
        else:
            print(-1)
    if command == 'size':
        print(len(q))
    if command == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    if command == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    if command == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)