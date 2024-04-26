from collections import deque

n, k = map(int, input().split())
r = []

q = deque([i for i in range(1, n+1)])
while q:
    q.rotate(-(k-1))
    r.append(q.popleft())
print('<', end='')
print(', '.join(map(str, r)), end='')
print('>')
