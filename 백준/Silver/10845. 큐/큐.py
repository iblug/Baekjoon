import sys
from collections import deque

input = sys.stdin.readline

def push(q, x):
    q.append(x)
def pop(q):
    if q:
        print(q.popleft())
    else:
        print(-1)
def size(q):
    print(len(q))
def empty(q):
    if q:
        print(0)
    else:
        print(1)
def front(q):
    if q:
        print(q[0])
    else:
        print(-1)
def back(q):
    if q:
        print(q[-1])
    else:
        print(-1)

N = int(input())
q = deque()

for _ in range(N):
    a, *x = input().split()
    if a == 'push':
        push(q, int(*x))
    elif a == 'pop':
        pop(q)
    elif a == 'size':
        size(q)
    elif a == 'empty':
        empty(q)
    elif a == 'front':
        front(q)
    elif a == 'back':
        back(q)
