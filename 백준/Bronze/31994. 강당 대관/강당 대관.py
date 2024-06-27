import sys
n = 0
s = ''
for _ in range(7):
    c, p = sys.stdin.readline().split()
    if n < int(p):
        n = int(p)
        s = c
print(s)