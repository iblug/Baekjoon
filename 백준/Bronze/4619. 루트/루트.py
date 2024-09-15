import sys
input = sys.stdin.readline

while 1:
    b, n = map(int, input().split())
    if not b*n:
        break
    t = 1
    while t ** n < b:
        t += 1
    print(t if t**n-b < b-(t-1)**n else t-1)