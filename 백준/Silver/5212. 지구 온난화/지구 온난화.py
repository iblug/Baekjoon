import sys
input = sys.stdin.readline

r, c = map(int, input().split())
g = [input().rstrip() for _ in range(r)]

dxy = ((0, 1),(1, 0),(0, -1),(-1, 0))
rows = [0 for _ in range(r)]
cols = [0 for _ in range(c)]
a = []
for i in range(r):
    m = ''
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
            if cnt > 2:
                m += '.'
            else:
                m += 'X'
        else:
            m += '.'
    if 'X' in m:
        s = m.index('X')
        e = c - list(reversed(m)).index('X')
        cols[s:e] = [1]*(e-s)
    a.append(m)
temp = list(zip(*a))
for i in temp:
    if 'X' in i:
        s = i.index('X')
        e = r - i[::-1].index('X')
        rows[s:e] = [1]*(e-s)

for i in range(r):
    for j in range(c):
        if rows[i] and cols[j]:
            print(a[i][j],end='')
    if rows[i]:
        print()