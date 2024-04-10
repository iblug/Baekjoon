import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
for _ in range(n):
    s = int(input()[2:])
    if s <= 90:
        cnt += 1

print(cnt)