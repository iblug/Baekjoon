import sys
input = sys.stdin.readline

n = int(input())
s = 0
for _ in range(n):
    a, b, c = map(int, input().split())
    if b > a:
        s += (b-a) * c
print(s)