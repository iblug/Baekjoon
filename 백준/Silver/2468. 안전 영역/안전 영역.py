import sys
input = sys.stdin.readline

def dfs(x, y):
    st = [(x, y)]
    while st:
        x, y = st.pop()
        if visited[x][y]:
            continue
        visited[x][y] = True
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0 > nx or nx >= n or 0 > ny or ny >= n:
                continue
            if not visited[nx][ny] and graph[nx][ny] > d:
                st.append((nx, ny))

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
M = max(map(max, graph))
m = min(map(min, graph))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

a = 0
for d in range(m-1, M):
    cnt = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
                if graph[i][j] > d and not visited[i][j]:
                    dfs(i, j)
                    cnt += 1
    a = max(a, cnt)

print(a)