import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(range(1, n+1))

for _ in range(m):
    a, b = map(int, input().split())
    m = (b-a)//2
    for i in range(m+1):
        arr[a+i-1] , arr[b-i-1] = arr[b-i-1], arr[a+i-1]

print(' '.join(map(str, arr)))    