import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, s, e = input().split()
    print(a[:int(s)] + a[int(e):])