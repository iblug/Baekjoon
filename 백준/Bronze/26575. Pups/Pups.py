import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a, b, c = map(float, input().split())
    print(f'${round(a*b*c, 2):.2f}')