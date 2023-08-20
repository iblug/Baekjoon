N, K = map(int, input().split())
d = list(map(int, input().split()))
s = [sum(d[:K])]
for k in range(N-K):
    s.append(s[k]-d[k]+d[k+K])
print(max(s))