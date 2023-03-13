c, r = map(int, input().split())
k = int(input())
if k > c*r:
    print(0)
    exit()

g = [[False]*(c+1) for _ in range(r+1)]
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
di = 0
sc = 1
sr = 1
g[1][1] = True
while k > 1:
    dc, dr = d[di]
    nc = sc + dc
    nr = sr + dr
    if nc <= 0 or nc > c or nr <= 0 or nr > r:
        di = (di+1)%4
        continue
    if g[nr][nc]:
        di = (di+1)%4
        continue
    g[nr][nc] = True
    k -= 1
    sc, sr = nc, nr
print(sc, sr)