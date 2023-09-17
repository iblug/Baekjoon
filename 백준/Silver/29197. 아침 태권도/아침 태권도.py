import sys
input = sys.stdin.readline

n = int(input())
d = set()
for _ in range(n):
    a, b = map(int, input().split())
    if a*b>0:
        q = 1
    else:
        q = 2
    d.add((q, b/a))
print(len(d))