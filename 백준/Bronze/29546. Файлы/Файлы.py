import sys
input = sys.stdin.readline

n = int(input())
a = [0]+[input().rstrip() for _ in range(n)]
m = int(input())
for _ in range(m):
    l, r = map(int, input().split())
    [print(a[i]) for i in range(l, r+1)]