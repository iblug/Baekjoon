# https://www.acmicpc.net/problem/10845
# 큐

import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

# def push(q, x):
#     q.append(x)
# def pop(q):
#     if q:
#         print(q.popleft())
#     else:
#         print(-1)
# def size(q):
#     print(len(q))
# def empty(q):
#     if q:
#         print(0)
#     else:
#         print(1)
# def front(q):
#     print(q[0])
# def back(q):
#     print(q[-1])

N = int(input())
q = deque()

for _ in range(N):
    a, *x = input().split()
    if a == 'push':
        # push(q, int(*x))
        q.append(int(*x))
    elif a == 'pop':
        # pop(q)
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif a == 'size':
        # size(q)
        print(len(q))
    elif a == 'empty':
        # empty(q)
        if q:
            print(0)
        else:
            print(1)
    elif a == 'front':
        # front(q)
        if q:
            print(q[0])
        else:
            print(-1)
    elif a == 'back':
        # back(q)
        if q:
            print(q[-1])
        else:
            print(-1)
    
# 함수형이나 바로 하는거랑 같음(속도도 같아보임, 메모리는 함수쪽이 작음)

# 문제 잘 읽자(fornt, back일때 if q)
# 출력도 sys.stdout.write 하면 더 빠름


# cmd = input().rstrip() 로 입력 받고
# push 일 때 q.append(cmd.split()[1]) 가능