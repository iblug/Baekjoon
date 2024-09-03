import sys
input = sys.stdin.readline

n, w, h = map(int, input().split())
for _ in range(n):
    l = int(input())
    if l > w and l > h and l > (w**2 + h**2)**0.5:
        print('NE')
    else:
        print('DA')