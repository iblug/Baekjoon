n, k, a, b = map(int, input().split())

c = [k]*n
d = 0
while True:
    d += 1
    c.sort()
    if c[a] == 1:
        break
    for i in range(a):
        c[i] += b-1
    for i in range(a, n):
        c[i] -= 1

print(d)