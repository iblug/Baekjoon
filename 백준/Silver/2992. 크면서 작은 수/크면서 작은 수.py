def p(s):
    u = [False]*l
    r = []
    def gen(c, u):
        if len(c) == l:
            c = int(c)
            if c > n:
                r.append(c)
            return
        for i in range(l):
            if not u[i]:
                c += s[i]
                if c == '0':
                    continue
                u[i] = True
                gen(c, u)
                c = c[:-1]
                u[i] = False
        return
    gen('', u)
    if r:
        print(min(r))
    else:
        print(0)

x = input()
l = len(x)
n = int(x)
p(x)