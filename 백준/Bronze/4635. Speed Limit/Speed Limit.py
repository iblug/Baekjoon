import sys
input = sys.stdin.readline

while 1:
    n = int(input())
    if n < 0:
        break
    t, r = 0, 0
    for _ in range(n):
        v, h = map(int, input().split())
        r += v*(h-t)
        t = h
    print(f'{r} miles')