import sys
input = sys.stdin.readline

n = int(input())
for t in range(1, n+1):
    print(f'Case #{t}: {max(map(int, input().split()))}')