import sys
input = sys.stdin.readline

N, M = map(int, input().split())
d = list(map(int, input().split()))
s = [0]
for i in range(N):
    s.append(s[i]+d[i])
r = []
for _ in range(M):
    i, j = map(int, input().split())
    r.append(s[j]-s[i-1])
print('\n'.join(map(str, r)))