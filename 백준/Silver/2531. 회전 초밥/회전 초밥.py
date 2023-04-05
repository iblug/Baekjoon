import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
a = [int(input()) for _ in range(n)]
a += a

r = 0
for i in range(n):
    eat = set(a[i:i+k])
    eat.add(c)
    if len(eat) > r:
        r = len(eat)
print(r)
