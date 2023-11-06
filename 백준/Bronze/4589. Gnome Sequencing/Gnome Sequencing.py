import sys
input = sys.stdin.readline

n = int(input())
print('Gnomes:')
for i in range(n):
    a, b, c = map(int, input().split())
    if a < b:
        if b < c:
            print('Ordered')
        else:
            print('Unordered')
    else:
        if b > c:
            print('Ordered')
        else:
            print('Unordered')