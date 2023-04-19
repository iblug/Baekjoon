import sys
input = sys.stdin.readline

dxy = ((0, 1),(1, 0),(0,-1),(-1, 0))

r, c, n = map(int, input().split())
g0 = [input().rstrip() for _ in range(r)]
g3 = [['O']*c for _ in range(r)]
g1 = [['O']*c for _ in range(r)]
for x in range(r):
    for y in range(c):
        if g0[x][y] == 'O':
            g3[x][y] = '.'
            for dx, dy in dxy:
                nx = x + dx
                ny = y + dy
                if nx < 0 or nx >= r or ny < 0 or ny >= c:
                    continue
                g3[nx][ny] = '.'
for x in range(r):
    for y in range(c):
        if g3[x][y] == 'O':
            g1[x][y] = '.'
            for dx, dy in dxy:
                nx = x + dx
                ny = y + dy
                if nx < 0 or nx >= r or ny < 0 or ny >= c:
                    continue
                g1[nx][ny] = '.'
if n == 1:
    print('\n'.join(g0))
elif n%4 == 1:
    for g in g1:
        print(''.join(g))
elif n%4 == 3:
    for g in g3:
        print(''.join(g))
else:
    [print('O'*c) for _ in range(r)]