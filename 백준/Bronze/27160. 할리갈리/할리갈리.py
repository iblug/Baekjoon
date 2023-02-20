import sys
input = sys.stdin.readline

n = int(input())
d = {}
for _ in range(n):
    a, b = input().split()
    d[a] = d.get(a,0) + int(b)
if 5 in d.values():
    print('YES')
else:
    print('NO')