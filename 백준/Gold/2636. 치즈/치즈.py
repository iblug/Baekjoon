
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    c = 0
    q = deque([(0,0)])
    v[0][0] = True
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if nx >= n or ny >= m or nx < 0 or ny < 0 or v[nx][ny]:
                continue
            if g[nx][ny] == '0':
                q.append((nx, ny))
            else:
                g[nx][ny] = '0'
                c += 1
            v[nx][ny] = 1
    if c:
        r[0] = c
        return False
    else:
        return True

dxy = ((0, 1), (1, 0), (0, -1), (-1, 0))

n, m = map(int, input().split())
g = [input().split() for _ in range(n)]

t = 0
r = [0]
while True:
    v = [[False]*m for _ in range(n)]
    if bfs():
        break
    t += 1
print(t, r[0], sep='\n')