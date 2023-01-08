import sys
input = sys.stdin.readline

t = int(input())

while t > 0:
    s = input().split()
    n = float(s[0])
    for i in s[1:]:
        if i == '@':
            n *= 3
        elif i == '%':
            n += 5
        elif i == '#':
            n -= 7
    print(f'{n:.2f}')
    t -= 1