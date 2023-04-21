import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    p = int(input())
    b = 0
    for _ in range(p):
        c, a = input().split()
        c = int(c)
        if int(c) > b:
            b = c
            r = a
    print(r)