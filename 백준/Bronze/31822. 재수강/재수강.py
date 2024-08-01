import sys
input = sys.stdin.readline

g = input()[:5]
n = int(input())
r = 0
for i in range(n):
    s = input()
    if s.startswith(g):
        r += 1
print(r)