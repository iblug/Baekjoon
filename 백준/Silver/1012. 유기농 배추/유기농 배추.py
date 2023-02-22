import sys
input = sys.stdin.readline

def dfs(x, y):
    s = [(x, y)]
    g[x][y] = 0
    while s:
        x, y = s.pop()
        for dx, dy in di:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if g[nx][ny]:
                s.append((nx, ny))
                g[nx][ny] = 0

def fnd():
    c = 0
    for i in range(N):
        for j in range(M):
            if g[i][j]:
                dfs(i, j)
                c += 1
    print(c)
    
T = int(input())
di = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for _ in range(T):
    M, N, K = map(int, input().split())
    g = [[0]*M for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        g[b][a] = 1
    fnd()