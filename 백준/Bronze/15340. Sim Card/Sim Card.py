import sys
input = sys.stdin.readline

t = [(30, 40), (35, 30), (40, 20)]

while 1:
    c, d = map(int, input().split())
    if not c*d:
        break
    r = 1e9
    for a, b in t:
        r = min(r, a*c+b*d)
    print(r)