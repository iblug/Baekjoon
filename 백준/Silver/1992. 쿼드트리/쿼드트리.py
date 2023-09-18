import sys
input = sys.stdin.readline

def b(n, x, y):
    if n == 1:
        return d[x][y]
    m = n//2
    d1 = d[x][y]
    f = True
    for i in range(x, x+n):
        for j in range(y, y+n):
            if d[i][j] != d1:
                f = False
                return '(' + b(m, x, y) + b(m, x, y+m) + b(m, x+m, y) + b(m, x+m, y+m) + ')'
    return d1
N = int(input())
d = [list(input().rstrip()) for _ in range(N)]

print(b(N, 0, 0))