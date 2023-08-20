N, K = map(int, input().split())
d = list(map(int, input().split()))
i = 0
j = K
s = [sum(d[i:j])]
while (j < N):
    s.append(s[i] + d[j] - d[i])
    j += 1
    i += 1
print(max(s))