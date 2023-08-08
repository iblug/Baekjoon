import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
s = deque()
for _ in range(N):
    a = input().split()
    match (a[0]):
        case '1':
            s.append(a[1])
        case '2':
            if s:
                print(s.pop())
            else:
                print(-1)
        case '3':
            print(len(s))
        case '4':
            if s:
                print(0)
            else:
                print(1)
        case '5':
            if s:
                print(s[-1])
            else:
                print(-1)