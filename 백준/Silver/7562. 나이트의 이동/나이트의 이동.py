import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, c):
    q = deque([(x, y, c)])
    v[x][y] = True
    while q:
        x, y, c = q.popleft()
        if (x, y) == D:
            return c
        for dx, dy in di:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= L or ny < 0 or ny >= L:
                continue
            if not v[nx][ny]:
                q.append((nx, ny, c+1))
                v[nx][ny] = True
    return c

T = int(input())
di = [(-2, 1),(-1, 2),(1, 2),(2, 1),(2, -1),(1, -2),(-1, -2),(-2, -1)]
for _ in range(T):    
    L = int(input())
    v = [[False]*L for _ in range(L)]
    cx, cy = map(int, input().split())
    D = tuple(map(int, input().split()))
    print(bfs(cx, cy, 0))