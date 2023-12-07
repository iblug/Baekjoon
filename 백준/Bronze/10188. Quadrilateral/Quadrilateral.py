import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    c, r = map(int, input().split())
    [print('X'*c) for _ in range(r)]
    print()