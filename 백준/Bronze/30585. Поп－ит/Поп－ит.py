import sys
input = sys.stdin.readline

h, w = map(int, input().split())
r = 0
for _ in range(h):
    r += sum(map(int, input().rstrip()))
print(min(r, h*w-r))