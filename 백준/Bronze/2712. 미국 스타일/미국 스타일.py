import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, d = input().split()
    if d == 'kg':
        print(f'{float(n)*2.2046:.4f}', 'lb')
    elif d == 'lb':
        print(f'{float(n)*0.4536:.4f}', 'kg')
    elif d == 'l':
        print(f'{float(n)*0.2642:.4f}', 'g')
    else:
        print(f'{float(n)*3.7854:.4f}', 'l')