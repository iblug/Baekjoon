import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a, b, c = map(int, input().split())
    print(f'Data set: {a} {b} {c}')
    for _ in range(c):
        if a > b:
            a = a / 2
        else:
            b = b / 2
    a, b = int(a), int(b)
    if a < b:
        a, b = b, a
    print(a, b)
    print()