w, n, p = map(int, input().split())
l = list(map(int, input().split()))
r = 0
for e in l:
    if w <= e <= n:
        r += 1
print(r)