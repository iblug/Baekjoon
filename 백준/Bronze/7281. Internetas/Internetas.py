import sys
input = sys.stdin.readline

n = int(input())
start, r = 0, 0

for _ in range(n):
    now, b = map(int, input().split())
    
    if b:
        r = max(r, now - start)
        start = now

print(r)