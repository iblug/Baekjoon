import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find_(n, x, y):
    if n == 1:
        return 0
    
    g = n//2
    nx = x + g
    ny = y + g
    if r < nx and c < ny:
        return find_(g, x, y)
    elif r < nx and c >= ny:
        return find_(g, x, ny) + g**2
    elif r >= nx and c < ny:
        return find_(g, nx, y) + (g**2)*2
    elif r >= nx and c >= ny:
        return find_(g, nx, ny) + (g**2)*3

N, r, c = map(int, input().split())
print(find_(2**N, 0, 0))