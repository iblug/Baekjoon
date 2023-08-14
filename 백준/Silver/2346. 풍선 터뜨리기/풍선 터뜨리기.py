from collections import deque

N = int(input())
d = deque(enumerate(map(int, input().split())))
r = []
while d:
    a, b = d.popleft()
    r.append(a+1)
    if b < 0:
        d.rotate(-b)
    else:
        d.rotate(-(b-1))
print(' '.join(map(str, r)))