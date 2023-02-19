import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y):
    visited[x][y] = True
    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]
        if 0 > nx or nx >= n or 0 > ny or ny >= n:
            continue
        if not visited[nx][ny] and graph[nx][ny] > d:
            dfs(nx, ny)

n = int(input())
s = set()
graph = []
m = 1e9
for _ in range(n):
    a = list(map(int, input().split()))
    m = min(m, min(a))
    graph.append(a)
    s.update(set(a))

s.add(m-1)
s = sorted(s)    

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

a = 0
for d in s:
    cnt = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
                if graph[i][j] > d and not visited[i][j]:
                    dfs(i, j)
                    cnt += 1
    a = max(a, cnt)

print(a)
