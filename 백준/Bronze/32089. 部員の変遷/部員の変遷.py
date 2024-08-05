import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if not n:
        break
    a = list(map(int, input().split()))
    t = r = sum(a[:3])
    for i in range(3, n):
        t += -a[i-3] + a[i]
        r = max(t, r)
    print(r)