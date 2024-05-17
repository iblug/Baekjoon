import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = map(float, input().split())
    print(f'The height of the triangle is {2*a/b:.2f} units')