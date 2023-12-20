import sys
input = sys.stdin.readline

s = 0
t = 101
for _ in range(4):
    n = int(input())
    if n < t:
        t = n
    s += n
s -= t
t = 101
for _ in range(2):
    n = int(input())
    if n < t:
        t = n
    s += n
s -= t
print(s)