import sys

input = sys.stdin.readline

N = int(input())
r = {}
for _ in range(N):
    a, b = input().split()
    r[a] = b

c = [i for i in r if r[i] == 'enter']
print('\n'.join(sorted(c, reverse=True)))