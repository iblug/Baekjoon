import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(f'Data set: {a} {b} {c}')
    for _ in range(c):
        if a > b:
            a, b = a//2, b
        else:
            a, b = a, b//2
    if a > b:
            a, b = b, a
    print(b, a)
    print()