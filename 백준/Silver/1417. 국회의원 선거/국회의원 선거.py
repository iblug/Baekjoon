import sys
input = sys.stdin.readline

n = int(input())
d = int(input())
c = [int(input()) for _ in range(n-1)]
cnt = 0
if n == 1:
    print(0)
else:
    while d <= max(c):
        c[c.index(max(c))] -= 1
        d += 1
        cnt += 1
    print(cnt)