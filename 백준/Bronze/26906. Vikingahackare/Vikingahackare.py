import sys
input = sys.stdin.readline

n = int(input())
d = {}
r = ''
for _ in range(n):
    a, b = input().split()
    d[b] = a
s = input().rstrip()
for i in range(0, len(s), 4):
    r += d.get(s[i:i+4], '?')
print(r)