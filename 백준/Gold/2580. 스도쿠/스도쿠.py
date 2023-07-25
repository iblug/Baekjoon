import sys
input = sys.stdin.readline

def s(bnk):
    if bnk == len(blank):
        for i in range(9):
            print(' '.join(map(str,b[i])))
        exit()
    x, y = blank[bnk]
    for i in range(1, 10):
        if check_r(x, i) and check_c(y, i) and check_b(x, y, i):
            b[x][y] = i
            s(bnk+1)
            b[x][y] = 0

def check_r(x, t):
    for i in range(9):
        if t == b[x][i]:
            return False
    return True

def check_c(y, t):
    for i in range(9):
        if t == b[i][y]:
            return False
    return True

def check_b(x, y, t):
    xx = x//3 * 3
    yy = y//3 * 3
    for i in range(3):
        for j in range(3):
            if b[xx+i][yy+j] == t:
                return False
    return True

b = [list(map(int, input().split())) for _ in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if b[i][j] == 0:
            blank.append((i, j))
s(0)
