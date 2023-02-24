import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [i for i in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a], arr[b] = arr[b], arr[a]
print(*arr[1:])