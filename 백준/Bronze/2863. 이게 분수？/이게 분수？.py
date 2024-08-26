a, b = map(int, input().split())
c, d = map(int, input().split())

m = 0
if m < a/c + b/d:
    m = a/c + b/d
    r = 0
if m < c/d + a/b:
    m = c/d + a/b
    r = 1
if m < d/b + c/a:
    m = d/b + c/a
    r = 2
if m < b/a + d/c:
    m = b/a + d/c
    r = 3

print(r)