import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e7))

def dfs(x, y):
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if ny >= N or nx >= N or nx < 0 or ny < 0:
            continue
        if v[nx][ny]:
            continue
        now = g[x][y]
        nxt = g[nx][ny]
        gap = abs(now-nxt)
        if L <= gap <= R:
            union.add((nx, ny))
            union_sum.append(g[nx][ny])
            v[nx][ny] = 1
            dfs(nx, ny)
    
N, L, R = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(N)]

dxy = ((0, 1), (1, 0), (0, -1), (-1, 0))

flag = 0
cnt = 0
while True:
    v = [[0]*N for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if not v[i][j]:
                union = set()
                union.add((i, j))
                union_sum = [g[i][j]]
                v[i][j] = 1
                dfs(i, j)
                if len(union) != 1:
                    flag = 1
                    p = sum(union_sum)//len(union)
                    for x, y in union:
                        g[x][y] = p
    if not flag:
        print(cnt)
        break
    cnt += 1