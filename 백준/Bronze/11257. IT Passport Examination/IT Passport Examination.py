import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a, s, m, t = map(int, input().split())
    f = 'PASS'
    if s < 35*0.3 or m < 25*0.3 or t < 40*0.3 or (s + m + t) < 55:
        f = 'FAIL'
    print(a, s + m + t, f)