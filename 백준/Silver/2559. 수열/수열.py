N, K = map(int, input().split())
d = list(map(int, input().split()))
s = [0]
r = []
for k in range(N):
    s.append(s[k]+d[k])
for k in range(N-K+1):
    r.append(s[k+K]-s[k])
print(max(r))
