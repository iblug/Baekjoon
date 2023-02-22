import sys
input = sys.stdin.readline

def dfs(x, y):
    s = [(x, y)]
    v[x][y] = True
    while s:
        x, y = s.pop()
        for dx, dy in di:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue
            if g[nx][ny] == '#' and not v[nx][ny]:
                s.append((nx, ny))
                v[nx][ny] = True

di = [(-1, 0), (1, 0), (0, -1), (0, 1)]
T = int(input())
for _ in range(T):
    H, W = map(int, input().split())
    g = [input().rstrip() for _ in range(H)]
    v = [[False]*W for _ in range(H)]
    c = 0
    for i in range(H):
        for j in range(W):
            if g[i][j] == '#' and not v[i][j]:
                dfs(i, j)
                c += 1
    print(c)