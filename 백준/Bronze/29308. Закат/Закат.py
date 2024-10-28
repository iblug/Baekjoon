import sys
input = sys.stdin.readline

n = int(input())
t = 0
for _ in range(n):
    a, b, c = input().split()
    if c == 'Russia' and int(a) > t:
        t = int(a)
        r = b
print(r)