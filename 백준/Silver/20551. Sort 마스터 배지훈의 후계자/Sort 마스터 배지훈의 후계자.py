import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = sorted(int(input()) for _ in range(n))

for _ in range(m):
    a = int(input())
    s = 0
    e = n-1
    while True:
        if s > e:
            if s >= n or d[s] != a:
                print(-1)
            else:
                print(s)
            break
        mid = (s+e) // 2
        if d[mid] >= a:
            e = mid-1
        elif d[mid] < a:
            s = mid+1