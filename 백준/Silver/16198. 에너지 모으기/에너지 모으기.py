def per(c, u, t):
    if len(c) == n-2:
        r.append(t)
        return
    for i in range(1, n-1):
        if not u[i]:
            u[i] = True
            c.append(i)
            p = 1
            while u[i+p]:
                p+=1
            m = 1
            while u[i-m]:
                m += 1
            t += w[i+p]*w[i-m]
            per(c, u, t)
            u[i] = False
            c.pop()
            t -= w[i+p]*w[i-m]

n = int(input())
w = list(map(int, input().split()))
u = [False]*n
r = []
per([], u, 0)
print(max(r))