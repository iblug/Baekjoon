import sys
input = sys.stdin.readline

while 1:
    n, m = map(int, input().split())
    if not n*m:
        break
    l = list(map(int, input().split()))
    r = 0
    for i in l:
        r += min(m//n, i)
    print(r)