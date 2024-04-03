import sys
input = sys.stdin.readline

n, d = map(int, input().split())
a = []
for _ in range(n):
    a.append(int(input()))
t = sum(a)

for e in a:
    print(d * e // t)