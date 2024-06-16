import sys
input = sys.stdin.readline

n = int(input())
a = [input().rstrip() for _ in range(n)]
m = int(input())
for _ in range(m):
    l, r = map(int, input().split())
    print('\n'.join(a[l-1:r]))