import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(x, y):
    global cnt
    d[x][y] += 1
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if d[nx][ny] == 1:
                d[nx][ny] = 2
                dfs(nx, ny)

n, m = map(int,input().split())

d = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = [0]
total = 0
for x in range(n):
    for y in range(m):
        if d[x][y] == 1:
            cnt = 0
            total += 1
            dfs(x, y)
            result.append(cnt)
print(total)
print(max(result))