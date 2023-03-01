import sys
from collections import deque
input = sys.stdin.readline

n, w, L = map(int, input().split())
t = list(map(int, input().split()))
q = deque([0]*w)

i = 0
time = 0
now = t[0]
while True:
    q.popleft()
    if sum(q) + now > L:
        q.append(0)
        time += 1
    else:
        q.append(now)
        time += 1
        i += 1
        if i < n:
            now=t[i]
        else:
            break
while q:
    q.popleft()
    time += 1
print(time)
