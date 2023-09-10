n, m = map(int, input().split())
a = list(map(int, input().split()))
o = [0]*m

s = 0
for i in range(n):
    s += a[i]
    o[s%m] += 1
r = 0
for i in range(m):
    r += o[i] * (o[i]-1) // 2
print(r+o[0])