import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = 0
    for _ in range(int(input())):
        n, v, p = input().split()
        v = int(v)
        p = float(p)
        s += v * p
    print(f'${s:.2f}')