import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    g, c, e = map(int, input().split())
    if c >= e:
        print(0)
    else:
        print((e-c)*(g*2-1))
