import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a = int(input())
    if a % 2:
        print(f'{a} is odd')
    else:
        print(f'{a} is even')