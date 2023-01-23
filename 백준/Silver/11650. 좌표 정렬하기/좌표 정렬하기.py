import sys
input = sys.stdin.readline
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
result = sorted(data, key = lambda x: (x[0], x[1]))
for r in result:
    print(*r)