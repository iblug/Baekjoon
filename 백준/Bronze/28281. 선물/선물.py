n, x = map(int, input().split())
s = list(map(int, input().split()))
r = 1e9
for i in range(n-1):
    t = s[i] + s[i+1]
    if r > t:
        r = t
print(r * x)