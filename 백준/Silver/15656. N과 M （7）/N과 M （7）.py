def per(a, r):
    a = sorted(a)
    def gen(c):
        if len(c) == m:
            print(' '.join(map(str, c)))
            return
        
        for i in a:
            c.append(i)
            gen(c)
            c.pop()
    gen([])

n, m = map(int, input().split())
a = list(map(int, input().split()))
per(a, m)