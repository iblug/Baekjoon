import sys
input = sys.stdin.readline

N = int(input())
s = []
for _ in range(N):
    s.append(list(map(int, input().split())))
s = sorted(s, key = lambda x:x[0])
s = sorted(s, key = lambda x:x[1])
for n in s:
    print(*n)