import sys

N = int(input())
s = -N+1
for _ in range(N):
    s += int(sys.stdin.readline().rstrip())
print(s)