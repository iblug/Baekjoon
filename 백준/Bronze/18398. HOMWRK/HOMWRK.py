import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    tt = int(input())
    for _ in range(tt):
        a, b = map(int, input().split())
        print(f'{a+b} {a*b}')