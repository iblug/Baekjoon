def per(u, l, w):
    global r
    if l == n:
        r += 1
        return
    w -= k
    for i in range(n):
        if not u[i]:
            if w+a[i] >= 0:
                u[i] = True
                per(u, l+1, w+a[i])
                u[i] = False

n, k = map(int, input().split())
a = list(map(int, input().split()))
u = [False] * n
r = 0
per(u,0,0)
print(r)