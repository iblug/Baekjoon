import sys
input = sys.stdin.readline

n = int(input())
s = input().split()
m, k = map(int, input().split())

P = set(i+1 for i, e in enumerate(s) if e == 'P')

for _ in range(m):
    a = set(map(int, input().split()))
    if not(a & P):
        print('W')
        break
else:
    print('P')