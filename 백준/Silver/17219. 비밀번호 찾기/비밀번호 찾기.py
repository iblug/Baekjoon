import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = dict(input().rstrip().split() for _ in range(n))

[print(data[input().rstrip()]) for _ in range(m)]