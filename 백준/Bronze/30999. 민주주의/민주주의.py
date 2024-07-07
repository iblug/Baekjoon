import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = 0
for _ in range(n):
    a = input()
    if a.count('O') > m/2:
        s += 1
print(s)