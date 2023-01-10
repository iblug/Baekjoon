a, b, c = map(int, input().split())
d = [0] * 101
for _ in range(3):
    i, o = map(int, input().split())
    for n in range(i, o):
        d[n] += 1
r = 0
r += d.count(1) * a
r += d.count(2) * b * 2
r += d.count(3) * c * 3
print(r)