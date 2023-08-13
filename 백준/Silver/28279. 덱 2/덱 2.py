import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
s = deque()
r = []
for _ in range(N):
    c = input().split()
    match (c[0]):
        case '1':
            s.append(c[1])
        case '2':
            s.appendleft(c[1])
        case '3':
            if s:
                r.append(s.pop())
            else:
                r.append('-1')
        case '4':
            if s:
                r.append(s.popleft())
            else:
                r.append('-1')
        case '5':
            r.append(str(len(s)))
        case '6':
            if s:
                r.append('0')
            else:
                r.append('1')
        case '7':
            if s:
                r.append(s[-1])
            else:
                r.append('-1')
        case '8':
            if s:
                r.append(s[0])
            else:
                r.append('-1')

print('\n'.join(r))