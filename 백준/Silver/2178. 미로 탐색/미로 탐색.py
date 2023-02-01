import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or nx >= n or 0 > ny or ny >= m:
                continue
            if graph[nx][ny] == 0 or graph[nx][ny] > 1:
                continue
            graph[nx][ny] = graph[x][y] + 1
            q.append((nx, ny))
    
n, m = map(int, input().split())

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = [list(map(int, input().rstrip())) for _ in range(n)]
bfs(0, 0)
print(graph[n-1][m-1])