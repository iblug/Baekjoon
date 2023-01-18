import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    s = input().split()
    for i in s:
        print(i[::-1], end=' ')
    print()