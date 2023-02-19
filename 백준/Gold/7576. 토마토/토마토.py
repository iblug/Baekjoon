import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not graph[nx][ny]:
                    q.append((nx, ny))
                    graph[nx][ny] = graph[x][y]+1

def check(g):
    max_ = 0
    for r in g:
        if 0 in r:
            return -1
        max_ = max(max_, max(r))
    return max_-1
m, n = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []
q = deque()
for i in range(n):
    a = list(map(int, input().split()))
    graph.append(a)
    for j in range(m):
        if a[j] == 1:
            q.append((i, j))
bfs()
print(check(graph))