a, b, c, m = map(int, input().split())

n = 0
w = 0
h = 0
while h < 24:
    if n + a <= m:
        n += a
        w += b
    else:
        n -= c
        if n < 0:
            n = 0
    h += 1

print(w)