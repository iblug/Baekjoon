import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
def dfs(x, y):
    global r
    graph[x][y] += 1
    r += 1
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n  and 0 <= ny < n:
            if graph[nx][ny] == 1:
                dfs(nx, ny) 

n = int(input())

graph = [list(map(int, list(input().rstrip()))) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
# r = 0
result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            r = 0
            dfs(i, j)
            result.append(r)
            cnt += 1
result.sort()
print(cnt, *result, sep='\n')