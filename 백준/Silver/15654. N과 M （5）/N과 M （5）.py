def p(a, r):
    a = sorted(a)
    a = list(map(str, a))
    v = [False]*n
    def gen(c:list, used):
        if len(c) == r:
            print(' '.join(c))
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
p(list(map(int, input().split())), m)