import sys
input = sys.stdin.readline

def find_(n, x, y):
    if n == 2:
        if x == r and y == c:
            return 0
        elif x == r and y+1 == c:
            return 1
        elif x+1 == r and y == c:
            return 2
        elif x+1 == r and y+1 == c:
            return 3
        
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