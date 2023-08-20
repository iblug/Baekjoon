import sys
input = sys.stdin.readline

N, M = map(int, input().split())
d = list(map(int, input().split()))
s = [0]
su = 0
for i in range(N):
    su += d[i]
    s.append(su)
r = []
for _ in range(M):
    i, j = map(int, input().split())
    r.append(s[j]-s[i-1])
print('\n'.join(map(str, r)))
