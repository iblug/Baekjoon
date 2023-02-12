import sys
input = sys.stdin.readline

def f(n,x,y):
    if N == 1:
        return data[0][0]
    if n == 2:
        tmp = [data[x][y], data[x+1][y], data[x][y+1], data[x+1][y+1]]
        tmp.sort()
        return tmp[1]
    else:
        g = n//2
        tmp = [
            f(g, x, y),
            f(g, x+g, y),
            f(g, x, y+g),
            f(g, x+g, y+g)
        ]
        tmp.sort()
        return tmp[1]
        

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

print(f(N,0,0))