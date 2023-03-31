import sys
input = sys.stdin.readline

n, m = map(int, input().split())
N = set(input().rstrip() for _ in range(n))
for _ in range(m):
    N -= set(input().rstrip().split(','))
    print(len(N))