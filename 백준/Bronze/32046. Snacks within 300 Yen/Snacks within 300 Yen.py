import sys
input = sys.stdin.readline

while 1:
    n = int(input())
    if not n:
        break
    l = list(map(int, input().split()))
    r = 0
    for e in l:
        if r + e <= 300:
            r += e
    print(r)