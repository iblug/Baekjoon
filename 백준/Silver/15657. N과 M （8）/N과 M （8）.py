def com(a):
    a = sorted(a)
    def gen(c):
        if len(c) == m:
            print(' '.join(map(str, c)))
            return
        start = a.index(c[-1]) if c else 0
        for i in range(start, n):
            c.append(a[i])
            gen(c)
            c.pop()
    gen([])

n, m = map(int, input().split())
a = list(map(int, input().split()))
com(a)