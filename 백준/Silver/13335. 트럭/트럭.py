import sys
from collections import deque
input = sys.stdin.readline

n, w, L = map(int, input().split())
t = list(map(int, input().split()))
q = deque([0]*w)

i = 0
time = 0
while i < n:
    q.popleft()
    now = t[i]
    if sum(q) + now > L:
        q.append(0)
    else:
        q.append(now)
        i += 1
    time += 1
while q:
    q.popleft()
    time += 1
print(time)
