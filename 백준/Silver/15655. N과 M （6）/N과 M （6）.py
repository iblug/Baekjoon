def com(a, r):
    a = sorted(a)
    u = [False] * n

    def gen(c):
        if len(c) == r:
            print(' '.join(map(str, c)))
            return
        
        s = a.index(c[-1]) if c else 0
        for i in range(s, n):
            if not u[i]:
                u[i] = True
                c.append(a[i])
                gen(c)
                u[i] = False
                c.pop()
    gen([])
n, m = map(int, input().split())
d = list(map(int, input().split()))
com(d, m)