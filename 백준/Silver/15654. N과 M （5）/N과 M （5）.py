def p(a, r):
    a = sorted(a)
    v = [False]*n
    def gen(c:list, used):
        if len(c) == r:
            print(*c)
            return

        for i in range(n):
            if not used[i]:
                used[i] = True
                c.append(a[i])
                gen(c, used)
                used[i] = False
                c.pop()
    gen([], v)

n, m = map(int, input().split())
a = list(map(int, input().split()))
p(a, m)