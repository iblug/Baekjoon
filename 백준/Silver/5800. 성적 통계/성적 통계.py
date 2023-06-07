import sys
input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    n, *s = map(int, input().split())
    s = sorted(s)
    gap = 0
    for i in range(n-1):
        g = s[i+1] - s[i]
        if g > gap:
            gap = g
    print(f'Class {t}\nMax {s[-1]}, Min {s[0]}, Largest gap {gap}')