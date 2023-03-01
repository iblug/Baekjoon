import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
data = [input().rstrip().replace(' ','') for _ in range(n)]

di = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visited = [[False]*m for _ in range(n)]

cnt = 0
ans = 0
while True:
    if not visited[r][c]:
        visited[r][c] = True
        ans += 1

    if cnt == 4:
        nr = r - di[d][0]
        nc = c - di[d][1]
        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            break
        if data[nr][nc] == '1':
            break
        r = nr
        c = nc
        cnt = 0

    d = (d+3)%4

    nr = r + di[d][0]
    nc = c + di[d][1]

    if nr < 0 or nr >= n or nc < 0 or nc >= m:
        cnt += 1
        continue
    if data[nr][nc] == '1' or visited[nr][nc]:
        cnt += 1
        continue
    r = nr
    c = nc
    cnt = 0

print(ans)