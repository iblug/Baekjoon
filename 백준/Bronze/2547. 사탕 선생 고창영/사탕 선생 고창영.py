import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    input()
    n = int(input())
    s = sum([int(input()) for _ in range(n)])
    if s % n:
        print('NO')
    else:
        print('YES')