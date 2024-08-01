import sys
input = sys.stdin.readline

g = input()
n = int(input())
r = 0
for i in range(n):
    s = input()
    if s.startswith(g[:5]):
        r += 1
print(r)