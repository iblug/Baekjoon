import sys
input = sys.stdin.readline

r, c = map(int, input().split())
g = [input().rstrip() for _ in range(r)]

dxy = ((0, 1),(1, 0),(0, -1),(-1, 0))

a = [['.']*c for _ in range(r)]
for i in range(r):
    for j in range(c):
        cnt = 0
        if g[i][j] == 'X':
            for dx, dy in dxy:
                nx = i + dx
                ny = j + dy
                if nx < 0:
                    cnt += 1
                elif nx >= r:
                    cnt += 1
                if ny < 0:
                    cnt += 1
                elif ny >= c:
                    cnt += 1
                if 0 <= nx < r and 0 <= ny < c:
                    if g[nx][ny] == '.':
                        cnt += 1
            if cnt <= 2:
                a[i][j] = 'X'

r_s , c_s = r, c
r_e = c_e = 0
for row in a:
    if 'X' in row:
        c_s = min(c_s, row.index('X'))
        c_e = max(c_e, c - row[::-1].index('X'))
temp = list(zip(*a))
for col in temp:
    if 'X' in col:
        r_s = min(r_s, col.index('X'))
        r_e = max(r_e, r - col[::-1].index('X'))
for i in range(r_s,r_e):
    print(''.join(a[i][c_s:c_e]))
