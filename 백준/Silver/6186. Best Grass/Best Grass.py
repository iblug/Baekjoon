import sys
input = sys.stdin.readline

def dfs(x,y):
    s = [(x, y)]
    v[x][y] = True
    while s:
        x, y = s.pop()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if not v[nx][ny] and g[nx][ny] == '#':
                s.append((nx, ny))
                v[nx][ny] = True

r, c = map(int, input().split())
g = [input().rstrip() for _ in range(r)]
v = [[False]*c for _ in range(r)]

d = ((-1, 0), (1, 0), (0, -1), (0, 1))

a = 0
for x in range(r):
    for y in range(c):
        if g[x][y] == '#' and not v[x][y]:
            dfs(x, y)
            a += 1
print(a)