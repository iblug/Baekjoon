import sys

input = sys.stdin.readline

N = int(input())
is_in = {}
for _ in range(N):
    a, b = input().split()
    is_in[a] = b
result = [i for i in is_in if is_in[i] == 'enter']

print('\n'.join(sorted(result, reverse=True)))