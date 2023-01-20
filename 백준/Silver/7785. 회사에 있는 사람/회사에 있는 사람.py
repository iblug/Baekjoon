import sys

input = sys.stdin.readline

N = int(input())
r = {}
for _ in range(N):
    a = input().rstrip()
    r[a[:-6]] = a[-1:]
c = [i for i in r if r[i] == 'r']
print('\n'.join(sorted(c, reverse=True)))