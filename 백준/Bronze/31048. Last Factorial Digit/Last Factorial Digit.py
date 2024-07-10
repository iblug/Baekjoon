import sys
input = sys.stdin.readline

t = int(input())
a = [0, 1, 2, 6, 4]
for _ in range(t):
    n = int(input())
    if n > 4:
        print(0)
    else:
        print(a[n])