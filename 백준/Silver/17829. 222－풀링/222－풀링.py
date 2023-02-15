import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def p(n, x, y):
    if n == 2:
        tmp = data[x][y:y+2] + data[x+1][y:y+2]
        tmp.sort()
        return tmp[-2]
    g = n//2
    tmp = [
        p(g, x, y),
        p(g, x+g, y),
        p(g, x, y+g),
        p(g, x+g, y+g)
    ]
    tmp.sort()
    return tmp[-2]

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

print(p(N, 0, 0))