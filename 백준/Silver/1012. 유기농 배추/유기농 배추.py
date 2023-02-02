import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x, y):
    graph[x][y] += 1
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1:
                dfs(nx, ny)

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())

    graph = [[0]*m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)