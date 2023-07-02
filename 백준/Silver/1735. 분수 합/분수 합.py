import sys
sys.setrecursionlimit(10**6)

def f(x, y):
    if x == 0:
        return y
    return f(y%x, x)

a, b = map(int, input().split())
c, d = map(int, input().split())

e = f(a*d+c*b, b*d)

print((a*d+c*b)//e, (b*d)//e)