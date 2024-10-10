import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    d, o, e = map(int, input().split())
    r = 0
    t = o*e
    print(d, o, e)
    r += d//o if d % o else d//o - 1
    r += d//e if d % e else d//e - 1
    while o%e != 0:
        o, e = e, o%e
    t = t//e
    r -= d//t if d % t else d//t - 1
    print(r)