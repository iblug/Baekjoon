import sys
input = sys.stdin.readline

def s(bnk):
    if bnk == len(blank):
        for i in range(9):
            print(' '.join(map(str,b[i])))
        exit()
    x, y = blank[bnk]
    c = check(x, y)
    for i in c:
        b[x][y] = i
        s(bnk+1)
        b[x][y] = 0

def check(x, y):
    s = {i for i in range(1, 10)}

    for i in range(9):
        if b[x][i] in s:
            s.discard(b[x][i])
        if b[i][y] in s:
            s.discard(b[i][y])
    xx = x//3 * 3
    yy = y//3 * 3
    for i in range(3):
        for j in range(3):
            if b[xx+i][yy+j] in s:
                s.discard(b[xx+i][yy+j])
    return s

b = [list(map(int, input().split())) for _ in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if b[i][j] == 0:
            blank.append((i, j))
s(0)