t = 0
m = 0
for _ in range(10):
    a, b = map(int, input().split())
    t += b - a
    if t > m:
        m = t
print(m)