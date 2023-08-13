import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
s = deque()
for _ in range(N):
    c = input().split()
    match (c[0]):
        case '1':
            s.append(c[1])
        case '2':
            s.appendleft(c[1])
        case '3':
            if s:
                print(s.pop())
            else:
                print(-1)
        case '4':
            if s:
                print(s.popleft())
            else:
                print(-1)
        case '5':
            print(len(s))
        case '6':
            if s:
                print(0)
            else:
                print(1)
        case '7':
            if s:
                print(s[-1])
            else:
                print(-1)
        case '8':
            if s:
                print(s[0])
            else:
                print(-1)