import sys
input = sys.stdin.readline

N, M = map(int, input().split())
d = {}
for _ in range(N):
    a = input().rstrip()
    if len(a) >= M:
        d[a] = d.get(a, 0) + 1
d = sorted(d.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for e in d:
    print(e[0])