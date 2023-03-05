def ba(x):
    if x == 0:
        print(' '.join(map(str, r)))
        return
    for i in range(1, n+1):
        if i not in v:
            v.add(i)
            r.append(i)
            ba(x-1)
            v.remove(i)
            r.pop()

n, m = map(int, input().split())

r = []
v = set()
ba(m)