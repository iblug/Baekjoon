import sys
input = sys.stdin.readline

def omok(x, y):
    for dx, dy in dxy:
        bx = x - dx
        by = y - dy
        if bx >= 0 and by >= 0 and bx < 19:
            if g[bx][by] == target:
                continue
        cnt = 0
        for i in range(1, 5):
            nx = x + dx*i
            ny = y + dy*i
            if nx >= 19 or ny >= 19 or nx < 0:
                break
            if g[nx][ny] != target:
                break
            else:
                cnt += 1
            if cnt == 4:
                nx += dx
                ny += dy
                if nx < 0 or nx >= 19 or ny >= 19 or g[nx][ny] != target:
                    return True
    return False

dxy = ((0, 1), (1, 0), (-1, 1), (1, 1))

g = [input().split() for _ in range(19)]
f = 0
for i in range(19):
    for j in range(19):
        if not g[i][j] == '0':
            target = g[i][j]
            if omok(i, j):
                print(target)
                print(i+1, j+1)
                f = 1
                break
    if f:
        break
if not f:
    print(0)